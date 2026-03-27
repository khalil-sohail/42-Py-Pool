import os


def ft_tqdm(lst: range) -> None:  # type: ignore
    total = len(lst)

    time_span_len = 25
    for i, item in enumerate(lst, 1):
        percent = int(100 * i / total)
        prefix = f"\r{percent}%|"
        suffix = f"| {i}/{total}"

        try:
            terminal_width = os.get_terminal_size().columns
        except OSError:
            terminal_width = 80

        bar_space = terminal_width - len(prefix) - len(suffix) - time_span_len
        filled_length = int(bar_space * i / total)
        bar = f"{'█' * filled_length}{' ' * (bar_space - filled_length)}"
        print(f"{prefix}{bar}{suffix}", end="", flush=True)

        yield item
