import csv

A3V3_ON_TRIGGER=0.5
VCAP_OFF_TRIGGER=3.015

data_vcap_a = []
data_a3v3_a = []
data_pfail = []
data_checkpoint = []
data_restore = []
data_d3v3 = []

def process_csv(csv_file):

    fields = None

    def get_time_idx(idx):
        if (idx == a3v3_a_idx):
            return idx-2
        return idx-1

    def add_data(row, data, idx):
        time_str = row[get_time_idx(idx)]
        if (time_str == ''):
            # No entry
            return
        data.append((float(time_str), float(row[idx])))


    # Parse csv
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        got_fields = False
        for row in reader:
            #print('Row:', row)
            if got_fields == False:
                fields = [r.strip() for r in row]

                # Configure the index
                vcap_a_idx = fields.index('VCap-Analog')
                a3v3_a_idx = fields.index('3V3A-Analog')
                pfail_idx = fields.index('PFail-Digital')
                checkpoint_idx = fields.index('Checkpoint-Digital')
                restore_idx = fields.index('Restore-Digital')
                d3v3_idx = fields.index('3V3D-Digital')

                got_fields = True
            else:
                row = [r.strip() for r in row]

                add_data(row, data_vcap_a, vcap_a_idx)
                add_data(row, data_a3v3_a, a3v3_a_idx)
                add_data(row, data_pfail, pfail_idx)
                add_data(row, data_checkpoint, checkpoint_idx)
                add_data(row, data_restore, restore_idx)
                add_data(row, data_d3v3, d3v3_idx)

                #sys.exit(0)

    print('Fields', fields)
    return

def lowpass_list(data_list, threshold=0.01):
    retlist = []
    for e in data_list:
        if abs(e[0] - e[1]) > threshold:
            retlist.append(e)
    return retlist

def lowpass_step(data_step, threshold=0.01):
    retstep = []
    time_last = -100.0
    for idx in range(len(data_step)-1):
        if data_step[idx][1] > 0.0:
            if data_step[idx+1][0]-data_step[idx][0] < threshold:
                continue
        retstep.append(data_step[idx])
    return retstep

# Compute the windows
# i.e. 1-1
def extract_low_high(data_list):
    low_list = []
    high_list = []

    last = 0.0

    for d in data_list:
        if d[1] == 0:
            high_list.append((last, d[0]))
        else:
            low_list.append((last, d[0]))

        last = d[0]

    return low_list, high_list

# Now we want to fit this to the active window
def fit_active_window(range_list):

    new_range_list = range_list.copy()

    for idx in range(len(new_range_list)):
        r = new_range_list[idx]
        mod = False
        for ah in active_high_list:
            #if r[0] <= ah[1] and r[1] <= ah[0]:
            #if max(r[0],ah[0]) <= min(r[1],ah[1]):

            #if ah[0] <= r[0] and ah[1] > r[0]:
            if r[0] > ah[0] and r[0] < ah[1]:
                # Begin fits, maybe trim end
                newx = r[0]
                newy = r[1]

                if r[0] < ah[0]:
                    newx = ah[0]

                if r[1] > ah[1]:
                    newy = ah[1]

                new_range_list[idx] = (newx, newy)
                mod = True

            if mod == False:
                new_range_list[idx] = (-1, -1)

    # Remove all the -1,-1 entries
    retlist = []
    for e in new_range_list:
        if e != (-1, -1):
            if abs(e[0] - e[1]) > 0.01: # The treshold TODO: Move this somewhere
                retlist.append(e)

    return retlist


pd_vcap_time = []
pd_vcap_voltage = []
pd_3v3a_time = []
pd_3v3a_voltage = []
pd_pfail_time = []
pd_pfail = []
pd_checkpoint_time = []
pd_checkpoint = []
pd_restore_time = []
pd_restore = []
pd_active_step_time = []
pd_active_step = []

pfail_low_list = []
pfail_high_list = []
active_high_list = []
active_low_list = []
pfail_fitted_low_list = []
restore_high_list = []
checkpoint_low_list = []
checkpoint_high_list = []
checkpoint_fitted_high_list = []

def process(data_file):
    global pd_vcap_time
    global pd_vcap_voltage
    global pd_3v3a_time
    global pd_3v3a_voltage
    global pd_pfail_time
    global pd_pfail
    global pd_checkpoint_time
    global pd_checkpoint
    global pd_restore_time
    global pd_restore
    global pd_active_step_time
    global pd_active_step

    global pfail_low_list
    global pfail_high_list
    global active_high_list
    global active_low_list
    global pfail_fitted_low_list
    global restore_high_list
    global checkpoint_low_list
    global checkpoint_high_list
    global checkpoint_fitted_high_list

    process_csv(data_file)

    # Prepare the data
    pd_vcap_time = [x[0] for x in data_vcap_a]
    pd_vcap_voltage = [x[1] for x in data_vcap_a]

    pd_3v3a_time = [x[0] for x in data_a3v3_a]
    pd_3v3a_voltage = [x[1] for x in data_a3v3_a]

    pd_pfail_time = [x[0] for x in data_pfail]
    pd_pfail = [x[1] for x in data_pfail]

    pd_checkpoint_time = [x[0] for x in data_checkpoint]
    pd_checkpoint = [x[1] for x in data_checkpoint]

    pd_restore_time = [x[0] for x in data_restore]
    pd_restore = [x[1] for x in data_restore]

    # The on-time is tricky as it is not until the signal dies.
    # This is becuase the NVM controller stops working at 1.8v
    # But because that is hard to correctly get we specify the turn-off in terms
    # of the cap voltage.
    pd_active_time = []
    pd_active = []
    for idx in range(len(pd_vcap_time)):
        pd_active_time.append(pd_3v3a_time[idx])

        if pd_3v3a_voltage[idx] > A3V3_ON_TRIGGER:
            if pd_vcap_voltage[idx] > VCAP_OFF_TRIGGER:
                pd_active.append(1.0)
            else:
                pd_active.append(0.0)
        else:
            pd_active.append(0.0)

    # Convert active to steps
    time = 0.0
    value = pd_active[0]
    data_active = []
    for idx in range(len(pd_active)):
        if pd_active[idx] != value:
            value = pd_active[idx]
            entry = (pd_active_time[idx], pd_active[idx])
            data_active.append(entry)

    #data_active_lp = lowpass_step(data_active, threshold=0.800)
    data_active_lp = data_active

    pd_active_step_time = [x[0] for x in data_active_lp]
    pd_active_step = [x[1] for x in data_active_lp]


    pfail_low_list, pfail_high_list = extract_low_high(data_pfail)

    active_low_list, active_high_list = extract_low_high(data_active_lp)


    pfail_fitted_low_list = fit_active_window(pfail_low_list)

    restore_low_list, restore_high_list = extract_low_high(data_restore)

    checkpoint_low_list, checkpoint_high_list = extract_low_high(data_checkpoint)
    checkpoint_fitted_high_list = fit_active_window(checkpoint_high_list)
