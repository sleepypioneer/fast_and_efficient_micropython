import time, machine,stm

led = machine.Pin('LED_BLUE')
N = 200_000

@micropython.asm_thumb
def blink_asm(r0):
    lsr(r0, r0, 3)
    movwt(r1, stm.GPIOB + stm.GPIO_BSRR)
    mov(r2, 1 << 4)
    label(loop)
    strh(r2, [r1, 0]) # high
    strh(r2, [r1, 2]) # low
    strh(r2, [r1, 0]) # high
    strh(r2, [r1, 2]) # low
    strh(r2, [r1, 0]) # high
    strh(r2, [r1, 2]) # low
    strh(r2, [r1, 0]) # high
    strh(r2, [r1, 2]) # low
    sub(r0, 1)
    bne(loop)

def time_it(f, n):
    t0 = time.ticks_us()
    f(n)
    t1 = time.ticks_us()
    dt = time.ticks_diff(t1, t0)
    fmt = '{:5.3f} sec, {:6.3f} usec/blink : {:8.2f} kblinks/sec'
    print(fmt.format(dt * 1e-6, dt / n, n /dt * 1e3))

time_it(blink_asm, N)