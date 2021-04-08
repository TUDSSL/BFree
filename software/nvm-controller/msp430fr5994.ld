/* ============================================================================ */
/* Copyright (c) 2015, Texas Instruments Incorporated                           */
/*  All rights reserved.                                                        */
/*                                                                              */
/*  Redistribution and use in source and binary forms, with or without          */
/*  modification, are permitted provided that the following conditions          */
/*  are met:                                                                    */
/*                                                                              */
/*  *  Redistributions of source code must retain the above copyright           */
/*     notice, this list of conditions and the following disclaimer.            */
/*                                                                              */
/*  *  Redistributions in binary form must reproduce the above copyright        */
/*     notice, this list of conditions and the following disclaimer in the      */
/*     documentation and/or other materials provided with the distribution.     */
/*                                                                              */
/*  *  Neither the name of Texas Instruments Incorporated nor the names of      */
/*     its contributors may be used to endorse or promote products derived      */
/*     from this software without specific prior written permission.            */
/*                                                                              */
/*  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" */
/*  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,       */
/*  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR      */
/*  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR            */
/*  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,       */
/*  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,         */
/*  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; */
/*  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,    */
/*  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR     */
/*  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,              */
/*  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                          */
/* ============================================================================ */

/* This file supports MSP430FR5994 devices. */
/* Default linker script, for normal executables */

/* 1.204 */

OUTPUT_ARCH(msp430)
ENTRY(_start)

MEMORY {
  TINYRAM          : ORIGIN = 0xA, LENGTH = 0x0016
  BSL              : ORIGIN = 0x1000, LENGTH = 0x0800
  RAM              : ORIGIN = 0x1C00, LENGTH = 0x1000
  LEARAM           : ORIGIN = 0x2C00, LENGTH = 0x0EC8
  LEASTACK         : ORIGIN = 0x3AC8, LENGTH = 0x0138
  INFOMEM          : ORIGIN = 0x1800, LENGTH = 0x0200
  INFOD            : ORIGIN = 0x1800, LENGTH = 0x0080
  INFOC            : ORIGIN = 0x1880, LENGTH = 0x0080
  INFOB            : ORIGIN = 0x1900, LENGTH = 0x0080
  INFOA            : ORIGIN = 0x1980, LENGTH = 0x0080
  ROM (rx)         : ORIGIN = 0x4000, LENGTH = 0xBF80 /* END=0xFF7F, size 49024 */
  HIFRAM (rxw)     : ORIGIN = 0x00010000, LENGTH = 0x00033FFF
  JTAGSIGNATURE    : ORIGIN = 0xFF80, LENGTH = 0x0004
  BSLSIGNATURE     : ORIGIN = 0xFF84, LENGTH = 0x0004
  IPESIGNATURE     : ORIGIN = 0xFF88, LENGTH = 0x0008
  VECT0           : ORIGIN = 0xFF90, LENGTH = 0x0002
  VECT1           : ORIGIN = 0xFF92, LENGTH = 0x0002
  VECT2           : ORIGIN = 0xFF94, LENGTH = 0x0002
  VECT3           : ORIGIN = 0xFF96, LENGTH = 0x0002
  VECT4           : ORIGIN = 0xFF98, LENGTH = 0x0002
  VECT5           : ORIGIN = 0xFF9A, LENGTH = 0x0002
  VECT6           : ORIGIN = 0xFF9C, LENGTH = 0x0002
  VECT7           : ORIGIN = 0xFF9E, LENGTH = 0x0002
  VECT8           : ORIGIN = 0xFFA0, LENGTH = 0x0002
  VECT9           : ORIGIN = 0xFFA2, LENGTH = 0x0002
  VECT10           : ORIGIN = 0xFFA4, LENGTH = 0x0002
  VECT11           : ORIGIN = 0xFFA6, LENGTH = 0x0002
  VECT12           : ORIGIN = 0xFFA8, LENGTH = 0x0002
  VECT13           : ORIGIN = 0xFFAA, LENGTH = 0x0002
  VECT14           : ORIGIN = 0xFFAC, LENGTH = 0x0002
  VECT15           : ORIGIN = 0xFFAE, LENGTH = 0x0002
  VECT16           : ORIGIN = 0xFFB0, LENGTH = 0x0002
  VECT17           : ORIGIN = 0xFFB2, LENGTH = 0x0002
  VECT18           : ORIGIN = 0xFFB4, LENGTH = 0x0002
  VECT19           : ORIGIN = 0xFFB6, LENGTH = 0x0002
  VECT20           : ORIGIN = 0xFFB8, LENGTH = 0x0002
  VECT21           : ORIGIN = 0xFFBA, LENGTH = 0x0002
  VECT22           : ORIGIN = 0xFFBC, LENGTH = 0x0002
  VECT23           : ORIGIN = 0xFFBE, LENGTH = 0x0002
  VECT24           : ORIGIN = 0xFFC0, LENGTH = 0x0002
  VECT25           : ORIGIN = 0xFFC2, LENGTH = 0x0002
  VECT26           : ORIGIN = 0xFFC4, LENGTH = 0x0002
  VECT27           : ORIGIN = 0xFFC6, LENGTH = 0x0002
  VECT28           : ORIGIN = 0xFFC8, LENGTH = 0x0002
  VECT29           : ORIGIN = 0xFFCA, LENGTH = 0x0002
  VECT30           : ORIGIN = 0xFFCC, LENGTH = 0x0002
  VECT31           : ORIGIN = 0xFFCE, LENGTH = 0x0002
  VECT32           : ORIGIN = 0xFFD0, LENGTH = 0x0002
  VECT33           : ORIGIN = 0xFFD2, LENGTH = 0x0002
  VECT34           : ORIGIN = 0xFFD4, LENGTH = 0x0002
  VECT35           : ORIGIN = 0xFFD6, LENGTH = 0x0002
  VECT36           : ORIGIN = 0xFFD8, LENGTH = 0x0002
  VECT37           : ORIGIN = 0xFFDA, LENGTH = 0x0002
  VECT38           : ORIGIN = 0xFFDC, LENGTH = 0x0002
  VECT39           : ORIGIN = 0xFFDE, LENGTH = 0x0002
  VECT40           : ORIGIN = 0xFFE0, LENGTH = 0x0002
  VECT41           : ORIGIN = 0xFFE2, LENGTH = 0x0002
  VECT42           : ORIGIN = 0xFFE4, LENGTH = 0x0002
  VECT43           : ORIGIN = 0xFFE6, LENGTH = 0x0002
  VECT44           : ORIGIN = 0xFFE8, LENGTH = 0x0002
  VECT45           : ORIGIN = 0xFFEA, LENGTH = 0x0002
  VECT46           : ORIGIN = 0xFFEC, LENGTH = 0x0002
  VECT47           : ORIGIN = 0xFFEE, LENGTH = 0x0002
  VECT48           : ORIGIN = 0xFFF0, LENGTH = 0x0002
  VECT49           : ORIGIN = 0xFFF2, LENGTH = 0x0002
  VECT50           : ORIGIN = 0xFFF4, LENGTH = 0x0002
  VECT51           : ORIGIN = 0xFFF6, LENGTH = 0x0002
  VECT52           : ORIGIN = 0xFFF8, LENGTH = 0x0002
  VECT53           : ORIGIN = 0xFFFA, LENGTH = 0x0002
  VECT54           : ORIGIN = 0xFFFC, LENGTH = 0x0002
  RESETVEC         : ORIGIN = 0xFFFE, LENGTH = 0x0002
}

_checkpoint_base_a = ORIGIN(HIFRAM);
_checkpoint_base_b = ORIGIN(HIFRAM) + 64k;

SECTIONS
{
  .leaRAM             : {} > LEARAM
  .jtagsignature      : {} > JTAGSIGNATURE
  .bslsignature       : {} > BSLSIGNATURE
  .ipe :
  {
    KEEP (*(.ipesignature))
    KEEP (*(.jtagpassword))
  } > IPESIGNATURE

  __interrupt_vector_0   : { KEEP (*(__interrupt_vector_0  )) } > VECT0
  __interrupt_vector_1   : { KEEP (*(__interrupt_vector_1  )) } > VECT1
  __interrupt_vector_2   : { KEEP (*(__interrupt_vector_2  )) } > VECT2
  __interrupt_vector_3   : { KEEP (*(__interrupt_vector_3  )) } > VECT3
  __interrupt_vector_4   : { KEEP (*(__interrupt_vector_4  )) } > VECT4
  __interrupt_vector_5   : { KEEP (*(__interrupt_vector_5  )) } > VECT5
  __interrupt_vector_6   : { KEEP (*(__interrupt_vector_6  )) } > VECT6
  __interrupt_vector_7   : { KEEP (*(__interrupt_vector_7  )) } > VECT7
  __interrupt_vector_8   : { KEEP (*(__interrupt_vector_8  )) } > VECT8
  __interrupt_vector_9   : { KEEP (*(__interrupt_vector_9  )) } > VECT9
  __interrupt_vector_10   : { KEEP (*(__interrupt_vector_10  )) } > VECT10
  __interrupt_vector_11   : { KEEP (*(__interrupt_vector_11  )) } > VECT11
  __interrupt_vector_12   : { KEEP (*(__interrupt_vector_12  )) } > VECT12
  __interrupt_vector_13   : { KEEP (*(__interrupt_vector_13  )) } > VECT13
  __interrupt_vector_14   : { KEEP (*(__interrupt_vector_14  )) } > VECT14
  __interrupt_vector_15   : { KEEP (*(__interrupt_vector_15  )) } > VECT15
  __interrupt_vector_16   : { KEEP (*(__interrupt_vector_16  )) } > VECT16
  __interrupt_vector_17   : { KEEP (*(__interrupt_vector_17  )) } > VECT17
  __interrupt_vector_18  : { KEEP (*(__interrupt_vector_18)) KEEP (*(__interrupt_vector_lea)) } > VECT18
  __interrupt_vector_19  : { KEEP (*(__interrupt_vector_19)) KEEP (*(__interrupt_vector_port8)) } > VECT19
  __interrupt_vector_20  : { KEEP (*(__interrupt_vector_20)) KEEP (*(__interrupt_vector_port7)) } > VECT20
  __interrupt_vector_21  : { KEEP (*(__interrupt_vector_21)) KEEP (*(__interrupt_vector_eusci_b3)) } > VECT21
  __interrupt_vector_22  : { KEEP (*(__interrupt_vector_22)) KEEP (*(__interrupt_vector_eusci_b2)) } > VECT22
  __interrupt_vector_23  : { KEEP (*(__interrupt_vector_23)) KEEP (*(__interrupt_vector_eusci_b1)) } > VECT23
  __interrupt_vector_24  : { KEEP (*(__interrupt_vector_24)) KEEP (*(__interrupt_vector_eusci_a3)) } > VECT24
  __interrupt_vector_25  : { KEEP (*(__interrupt_vector_25)) KEEP (*(__interrupt_vector_eusci_a2)) } > VECT25
  __interrupt_vector_26  : { KEEP (*(__interrupt_vector_26)) KEEP (*(__interrupt_vector_port6)) } > VECT26
  __interrupt_vector_27  : { KEEP (*(__interrupt_vector_27)) KEEP (*(__interrupt_vector_port5)) } > VECT27
  __interrupt_vector_28  : { KEEP (*(__interrupt_vector_28)) KEEP (*(__interrupt_vector_timer4_a1)) } > VECT28
  __interrupt_vector_29  : { KEEP (*(__interrupt_vector_29)) KEEP (*(__interrupt_vector_timer4_a0)) } > VECT29
  __interrupt_vector_30  : { KEEP (*(__interrupt_vector_30)) KEEP (*(__interrupt_vector_aes256)) } > VECT30
  __interrupt_vector_31  : { KEEP (*(__interrupt_vector_31)) KEEP (*(__interrupt_vector_rtc_c)) } > VECT31
  __interrupt_vector_32  : { KEEP (*(__interrupt_vector_32)) KEEP (*(__interrupt_vector_port4)) } > VECT32
  __interrupt_vector_33  : { KEEP (*(__interrupt_vector_33)) KEEP (*(__interrupt_vector_port3)) } > VECT33
  __interrupt_vector_34  : { KEEP (*(__interrupt_vector_34)) KEEP (*(__interrupt_vector_timer3_a1)) } > VECT34
  __interrupt_vector_35  : { KEEP (*(__interrupt_vector_35)) KEEP (*(__interrupt_vector_timer3_a0)) } > VECT35
  __interrupt_vector_36  : { KEEP (*(__interrupt_vector_36)) KEEP (*(__interrupt_vector_port2)) } > VECT36
  __interrupt_vector_37  : { KEEP (*(__interrupt_vector_37)) KEEP (*(__interrupt_vector_timer2_a1)) } > VECT37
  __interrupt_vector_38  : { KEEP (*(__interrupt_vector_38)) KEEP (*(__interrupt_vector_timer2_a0)) } > VECT38
  __interrupt_vector_39  : { KEEP (*(__interrupt_vector_39)) KEEP (*(__interrupt_vector_port1)) } > VECT39
  __interrupt_vector_40  : { KEEP (*(__interrupt_vector_40)) KEEP (*(__interrupt_vector_timer1_a1)) } > VECT40
  __interrupt_vector_41  : { KEEP (*(__interrupt_vector_41)) KEEP (*(__interrupt_vector_timer1_a0)) } > VECT41
  __interrupt_vector_42  : { KEEP (*(__interrupt_vector_42)) KEEP (*(__interrupt_vector_dma)) } > VECT42
  __interrupt_vector_43  : { KEEP (*(__interrupt_vector_43)) KEEP (*(__interrupt_vector_eusci_a1)) } > VECT43
  __interrupt_vector_44  : { KEEP (*(__interrupt_vector_44)) KEEP (*(__interrupt_vector_timer0_a1)) } > VECT44
  __interrupt_vector_45  : { KEEP (*(__interrupt_vector_45)) KEEP (*(__interrupt_vector_timer0_a0)) } > VECT45
  __interrupt_vector_46  : { KEEP (*(__interrupt_vector_46)) KEEP (*(__interrupt_vector_adc12_b)) } > VECT46
  __interrupt_vector_47  : { KEEP (*(__interrupt_vector_47)) KEEP (*(__interrupt_vector_eusci_b0)) } > VECT47
  __interrupt_vector_48  : { KEEP (*(__interrupt_vector_48)) KEEP (*(__interrupt_vector_eusci_a0)) } > VECT48
  __interrupt_vector_49  : { KEEP (*(__interrupt_vector_49)) KEEP (*(__interrupt_vector_wdt)) } > VECT49
  __interrupt_vector_50  : { KEEP (*(__interrupt_vector_50)) KEEP (*(__interrupt_vector_timer0_b1)) } > VECT50
  __interrupt_vector_51  : { KEEP (*(__interrupt_vector_51)) KEEP (*(__interrupt_vector_timer0_b0)) } > VECT51
  __interrupt_vector_52  : { KEEP (*(__interrupt_vector_52)) KEEP (*(__interrupt_vector_comp_e)) } > VECT52
  __interrupt_vector_53  : { KEEP (*(__interrupt_vector_53)) KEEP (*(__interrupt_vector_unmi)) } > VECT53
  __interrupt_vector_54  : { KEEP (*(__interrupt_vector_54)) KEEP (*(__interrupt_vector_sysnmi)) } > VECT54
  __reset_vector         : { KEEP (*(__interrupt_vector_55)) KEEP (*(__interrupt_vector_reset)) KEEP (*(.resetvec)) } > RESETVEC

  .lower.rodata :
  {
    . = ALIGN(2);
    *(.lower.rodata.* .lower.rodata)
  } > ROM

  .rodata :
  {
    . = ALIGN(2);
    *(.plt)
    *(.rodata .rodata.* .gnu.linkonce.r.* .const .const:*)
    *(.rodata1)
	/* Note: By default we do not have this line:

         *(.either.rodata.*) *(.either.rodata)

       defined here, or anywhere else in this script.  This is deliberate.
       The algorithm in the linker that automatically places rodata into
       either the .rodata or the .upper.rodata sections relies upon the
       fact that the .either.rodata section is not defined, and that the
       .upper.rodata section is defined.  If the .upper.rodata is not
       defined in this script then the line above should be restored so that
       code compiled with -mdata-region=either enabled will still work.

       The same reasoning applies to the absence of definitions for the
       .either.text, .either.data and .either.bss sections as well.  */

    KEEP (*(.gcc_except_table)) *(.gcc_except_table.*)
    PROVIDE (__preinit_array_start = .);
    KEEP (*(.preinit_array))
    PROVIDE (__preinit_array_end = .);
    PROVIDE (__init_array_start = .);
    KEEP (*(SORT(.init_array.*)))
    KEEP (*(.init_array))
    PROVIDE (__init_array_end = .);
    PROVIDE (__fini_array_start = .);
    KEEP (*(.fini_array))
    KEEP (*(SORT(.fini_array.*)))
    PROVIDE (__fini_array_end = .);
  } > ROM

  /* Note: Separate .rodata section for sections which are
     read only but which older linkers treat as read-write.
     This prevents older linkers from marking the entire .rodata
     section as read-write.  */
  .rodata2 : {
    . = ALIGN(2);
    *(.eh_frame_hdr)
    KEEP (*(.eh_frame))	
    /* gcc uses crtbegin.o to find the start of the constructors, so
       we make sure it is first.  Because this is a wildcard, it
       doesn't matter if the user does not actually link against
       crtbegin.o; the linker won't look for a file to match a
       wildcard.  The wildcard also means that it doesn't matter which
       directory crtbegin.o is in.  */
    KEEP (*crtbegin*.o(.ctors))

    /* We don't want to include the .ctor section from from the
       crtend.o file until after the sorted ctors.  The .ctor section
       from the crtend file contains the end of ctors marker and it
       must be last */
    KEEP (*(EXCLUDE_FILE (*crtend*.o ) .ctors))
    KEEP (*(SORT(.ctors.*)))
    KEEP (*(.ctors))

    KEEP (*crtbegin*.o(.dtors))
    KEEP (*(EXCLUDE_FILE (*crtend*.o ) .dtors))
    KEEP (*(SORT(.dtors.*)))
    KEEP (*(.dtors))
  } > ROM
  
  /* This section contains data that is not initialised during load
     or application reset. */
  .persistent :
  {
    . = ALIGN(2);
    PROVIDE (__persistent_start = .);
    *(.persistent)
    . = ALIGN(2);
    PROVIDE (__persistent_end = .);
  } > ROM
  
  .upper.rodata :
  {
    /* Note: If this section is not defined then please add:

           *(.either.rodata.*) *(.either.rodata)

       to the definition of the .rodata section above.  This
       will allow code compiled with -mdata-region=either to
       work properly.  */
    *(.upper.rodata.* .upper.rodata)
  } > HIFRAM

  .tinyram : {} > TINYRAM

  .lower.data :
  {
    . = ALIGN(2);
    PROVIDE (__datastart = .);
    *(.lower.data.* .lower.data)
  } > RAM AT> ROM

  .data :
  {
    . = ALIGN(2);
    PROVIDE (__datastart = .);

    KEEP (*(.jcr))
    *(.data.rel.ro.local) *(.data.rel.ro*)
    *(.dynamic)

    *(.data .data.* .gnu.linkonce.d.*)
    KEEP (*(.gnu.linkonce.d.*personality*))
    SORT(CONSTRUCTORS)
    *(.data1)
    *(.got.plt) *(.got)

    /* We want the small data sections together, so single-instruction offsets
       can access them all, and initialized data all before uninitialized, so
       we can shorten the on-disk segment size.  */
    . = ALIGN(2);
    *(.sdata .sdata.* .gnu.linkonce.s.* D_2 D_1)

    /* See the note in .rodata section about why we do not have this line here:

        *(.either.data.* .either.data)
    */
    . = ALIGN(2);
    _edata = .;
    PROVIDE (edata = .);
    PROVIDE (__dataend = .);
  } > RAM AT> ROM

  /* Note that crt0 assumes this is a multiple of two; all the
     start/stop symbols are also assumed word-aligned.  */
  PROVIDE(__romdatastart = LOADADDR(.lower.data));
  PROVIDE (__romdatacopysize = SIZEOF(.lower.data) + SIZEOF(.data));

  .upper.data :
  {
    __upper_data_init = LOADADDR (.upper.data);
    /* Status word.  */
    SHORT(1);
    __high_datastart = .;
    *(.upper.data.* .upper.data)
    __high_dataend = .;
  } > HIFRAM AT> ROM

  __rom_highdatacopysize = SIZEOF(.upper.data) - 2;
  __rom_highdatastart = LOADADDR(.upper.data) + 2;

  .lower.bss :
  {
    . = ALIGN(2);
    PROVIDE (__bssstart = .);
    *(.lower.bss.* .lower.bss)
  } > RAM

  .bss :
  {
    . = ALIGN(2);
    PROVIDE (__bssstart = .);
    *(.dynbss)
    *(.sbss .sbss.*)
    *(.bss .bss.* .gnu.linkonce.b.*)
    /* See the note in .rodata section about why we do not have this line here:

        *(.either.bss.* .either.bss)
    */
    . = ALIGN(2);
    *(COMMON)
    PROVIDE (__bssend = .);
  } > RAM
  PROVIDE (__bsssize = SIZEOF(.lower.bss) + SIZEOF(.bss));
  /* This section contains data that is not initialised during load
     or application reset.  */
  .noinit (NOLOAD) :
  {
    . = ALIGN(2);
    PROVIDE (__noinit_start = .);
    *(.noinit)
    . = ALIGN(2);
    PROVIDE (__noinit_end = .);
  } > RAM

  .upper.bss :
  {
    /* Note - if this section is not going to be defined then please
       add this line back into the definition of the .bss section above:

         *(.either.bss.* .either.bss)
    */
    . = ALIGN(2);
    __high_bssstart = .;
    *(.upper.bss.* .upper.bss)
    . = ALIGN(2);
    __high_bssend = .;
  } > HIFRAM
  __high_bsssize = SIZEOF(.upper.bss);

  /* We create this section so that "end" will always be in the
     RAM region (matching .stack below), even if the .bss
     section is empty.  */
  .heap (NOLOAD) :
  {
    . = ALIGN(2);
    __heap_start__ = .;
    _end = __heap_start__;
    PROVIDE (end = .); 
    KEEP (*(.heap))
    _end = .;
    PROVIDE (end = .);
    /* This word is here so that the section is not empty, and thus
       not discarded by the linker.  The actual value does not matter
       and is ignored.  */
    LONG(0);
    __heap_end__ = .;
    __HeapLimit = __heap_end__;
  } > RAM
  /* WARNING: Do not place anything in RAM here.
     The heap section must be the last section in RAM and the stack
     section must be placed at the very end of the RAM region.  */
  .stack (ORIGIN (RAM) + LENGTH(RAM)) :
  {
    PROVIDE (__stack = .);
    *(.stack)
  }

  .lower.text :
  {
    . = ALIGN(2);
    *(.lower.text.* .lower.text)
  } > ROM

  .text :
  {
    PROVIDE (_start = .);

    . = ALIGN(2);
    KEEP (*(SORT(.crt_*)))

    . = ALIGN(2);
    *(.lower.text.* .lower.text)

    . = ALIGN(2);
    *(.text .stub .text.* .gnu.linkonce.t.* .text:*)
    /* See the note in .rodata section about why we do not have this line here:

        *(.either.text.* .either.text)

    */

    KEEP (*(.text.*personality*))
    /* .gnu.warning sections are handled specially by elf32.em.  */
    *(.gnu.warning)
    *(.interp .hash .dynsym .dynstr .gnu.version*)
    PROVIDE (__etext = .);
    PROVIDE (_etext = .);
    PROVIDE (etext = .);
    . = ALIGN(2);
    KEEP (*(.init))
    KEEP (*(.fini))
    KEEP (*(.tm_clone_table))
  } > ROM

  .upper.text :
  {
    /* Note - if this section is not going to be included in the script
       then please add this line back into the definition of the .text
       section above:

         *(.either.text.* .either.text)
    */
    . = ALIGN(2);
    *(.upper.text.* .upper.text)
  } > HIFRAM

  /* MSP430 INFO FLASH MEMORY SEGMENTS */
  .infoD (NOLOAD) : {} > INFOD
  .infoC (NOLOAD) : {} > INFOC
  .infoB (NOLOAD) : {} > INFOB
  .infoA (NOLOAD) : {} > INFOA


  /* The rest are all not normally part of the runtime image.  */

  .MSP430.attributes 0 :
  {
    KEEP (*(.MSP430.attributes))
    KEEP (*(.gnu.attributes))
    KEEP (*(__TI_build_attributes))
  }

  /* Stabs debugging sections.  */
  .stab          0 : { *(.stab) }
  .stabstr       0 : { *(.stabstr) }
  .stab.excl     0 : { *(.stab.excl) }
  .stab.exclstr  0 : { *(.stab.exclstr) }
  .stab.index    0 : { *(.stab.index) }
  .stab.indexstr 0 : { *(.stab.indexstr) }
  .comment       0 : { *(.comment) }
  /* DWARF debug sections.
     Symbols in the DWARF debugging sections are relative to the beginning
     of the section so we begin them at 0.  */
  /* DWARF 1.  */
  .debug          0 : { *(.debug) }
  .line           0 : { *(.line) }
  /* GNU DWARF 1 extensions.  */
  .debug_srcinfo  0 : { *(.debug_srcinfo) }
  .debug_sfnames  0 : { *(.debug_sfnames) }
  /* DWARF 1.1 and DWARF 2.  */
  .debug_aranges  0 : { *(.debug_aranges) }
  .debug_pubnames 0 : { *(.debug_pubnames) }
  /* DWARF 2.  */
  .debug_info     0 : { *(.debug_info .gnu.linkonce.wi.*) }
  .debug_abbrev   0 : { *(.debug_abbrev) }
  .debug_line     0 : { *(.debug_line .debug_line.* .debug_line_end ) }
  .debug_frame    0 : { *(.debug_frame) }
  .debug_str      0 : { *(.debug_str) }
  .debug_loc      0 : { *(.debug_loc) }
  .debug_macinfo  0 : { *(.debug_macinfo) }
  /* SGI/MIPS DWARF 2 extensions.  */
  .debug_weaknames 0 : { *(.debug_weaknames) }
  .debug_funcnames 0 : { *(.debug_funcnames) }
  .debug_typenames 0 : { *(.debug_typenames) }
  .debug_varnames  0 : { *(.debug_varnames) }
  /* DWARF 3 */
  .debug_pubtypes 0 : { *(.debug_pubtypes) }
  .debug_ranges   0 : { *(.debug_ranges) }
  /* DWARF Extension.  */
  .debug_macro    0 : { *(.debug_macro) }

  /DISCARD/ : { *(.note.GNU-stack) }
}

/****************************************************************************/
/* Include peripherals memory map                                           */
/****************************************************************************/

INCLUDE msp430fr5994_symbols.ld

