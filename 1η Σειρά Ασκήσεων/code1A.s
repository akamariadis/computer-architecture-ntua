min:
    lw   $t0, 0($a0)
    li   $t1, 1

loop:
    bge  $t1, $a1, end
    sll  $t2, $t1, 2
    add  $t3, $a0, $t2
    lw   $t4, 0($t3)
    blt  $t4, $t0, update
    j    next

update:
    move $t0, $t4 

next:
    addi $t1, $t1, 1
    j    loop

end:
    move $v0, $t0 
    jr   $ra
