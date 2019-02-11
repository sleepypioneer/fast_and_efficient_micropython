import time, machine

led = machine.Pin('LED_BLUE')
N = 200_000

def blink_preload_unrolled4(n):
    n //= 4
    on = led.on
    off = led.off
    r = range(n)
    for i in r:
        on()
        off()
        on()
        off()
        on()
        off()
        on()
        off()

def time_it(f, n):
    t0 = time.ticks_us()
    f(n)
    t1 = time.ticks_us()
    dt = time.ticks_diff(t1, t0)
    fmt = '{:5.3f} sec, {:6.3f} usec/blink : {:8.2f} kblinks/sec'
    print(fmt.format(dt * 1e-6, dt / n, n /dt * 1e3))

time_it(blink_preload_unrolled4, N)




