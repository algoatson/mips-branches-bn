from binaryninja import *
for func in bv.functions:
    for block in func.basic_blocks:
        for inst in block.get_disassembly_text():
            if inst.tokens[0].text == 'nop':
                print(f"Highlighted Unused Delay-Slot at {inst.address:#x}")
                func.set_auto_instr_highlight(
                    inst.address,
                    HighlightStandardColor.MagentaHighlightColor
                )
                func.set_auto_instr_highlight(
                    inst.address-8,
                    HighlightStandardColor.GreenHighlightColor
                )
