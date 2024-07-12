import time


def main():
    pass


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f"{time.perf_counter() - start}s")
