import _thread, time


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def test_fib(n):
    print(f'Fib {n}: {fibonacci(n)}')


def run_fibs():
    test_fib(35)
    test_fib(10)
    test_fib(30)


def run_fibs_with_threads():
    _thread.start_new_thread(test_fib, (35,))
    _thread.start_new_thread(test_fib, (10,))
    _thread.start_new_thread(test_fib, (30,))
    time.sleep(12)


#run_fibs()
run_fibs_with_threads()