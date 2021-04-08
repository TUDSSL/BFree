import board
import digitalio
import time
import checkpoint

# Benchmark pins
pin_start = digitalio.DigitalInOut(board.D4)
pin_start.pull = digitalio.Pull.DOWN

pin_done = digitalio.DigitalInOut(board.D5)
pin_done.direction = digitalio.Direction.OUTPUT
pin_done.value = False

def Fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

# 512: 27745922289305716855338470916082815029348872029647830861914852073402148308000613611082094085891168867554589
# 1024: 2785293550699592923938812412668093509353307352123703806913182668987369503203465183625616759613324452749958549669966882191117895425015208455469403731272652158240825628484818131485544230827304940519132195299466733282
# 2048: 28068201751760541113209004611892322766557926801556756419424083986968314714727996157172546032929843372458753527397061344919986587417493110533831455616883457997685486582628983650599293908141932830226744480342923081054982198248114597831835076494600759283135301047068769273254907441767834557840730669852366903243155053389115511728868808387866489766103499938045875538224232660173988434766403992071664006121698686127581562214298380573
# 4096: 2850373826722699597173047515750950593339178089043511895137676653694047178307023910244889688443923619586163564890291999691174417024782600893477697489924562166680828606802634548464331897181658510148111056162766933169520537683589227271383574448892707393281387825428758589545570963756226815561575465627342116167674931728201653183719209149091743782992316003895770932145332642165474882396512935028568446137124573494259869604030715351481211755494149004960255047991424281237627530932218381477169473888085346068072326515595101330625934987442426337170649219214904388632085787949340251055116795473060067211352628230044499353966401523256734886996367786593974218627402850903996180240806716706006012047132476658042620896648409781259072159305246540984806591769930091337127340669099627391992639214113826403976892604856272745941282798757994891141679783399150094507261986530

num = 40
result = 0

####
#### Benchmark start
####

# Uncomment for the trigger benchmark
checkpoint.set_schedule(1)

checkpoint.disable()

restore_count_start = checkpoint.restore_count()
checkpoint_count_start = checkpoint.checkpoint_count()

# Uncomment when using a logic analyzer, comment out if using Teensy power toggler
pin_done.value = True

#while pin_start.value != True:
#    pass

# Start signal
pin_done.value = False

checkpoint.enable()

for i in range(0,30000):
    result = Fibonacci(num)


# The benchmark is done, set the done signal
pin_done.value = True

# Print some info
checkpoint_count = checkpoint.checkpoint_count() - checkpoint_count_start
restore_count = checkpoint.restore_count() - restore_count_start

while True:
    print('Checkpoint count:', checkpoint_count)
    print('Restore count:', restore_count)
    print(str(checkpoint_count) + ', ' + str(restore_count))
    time.sleep(1)