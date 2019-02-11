import time, machine,stm

led = machine.Pin('LED_BLUE')
N = 200_000

@micropython.viper
def blink_unrolled8_viper(n:int):
    n //= 4
    p = ptr16(stm.GPIOB + stm.GPIO_BSRR)
    for i in range(n):
        p[0] = 1 << 4 # high
        p[1] = 1 << 4 # low
        p[0] = 1 << 4 # high
        p[1] = 1 << 4 # low
        p[0] = 1 << 4 # high
        p[1] = 1 << 4 # low
        p[0] = 1 << 4 # high
        p[1] = 1 << 4 # low


def time_it(f, n):
    t0 = time.ticks_us()
    f(n)
    t1 = time.ticks_us()
    dt = time.ticks_diff(t1, t0)
    fmt = '{:5.3f} sec, {:6.3f} usec/blink : {:8.2f} kblinks/sec'
    print(fmt.format(dt * 1e-6, dt / n, n /dt * 1e3))

time_it(blink_unrolled8_viper, N)