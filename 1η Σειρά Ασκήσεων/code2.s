BitCount:
    addi $sp, $sp, -8
    sw   $ra, 4($sp)
    sw   $t0, 0($sp)

    beq  $a0, $0, base_case

    andi $t0, $a0, 1
    srl  $a0, $a0, 1
    jal  BitCount

    add  $v0, $v0, $t0
    j    BitCount_end

base_case:
    li   $v0, 0

BitCount_end:
    lw   $t0, 0($sp)
    lw   $ra, 4($sp)
    addi $sp, $sp, 8
    jr   $ra
