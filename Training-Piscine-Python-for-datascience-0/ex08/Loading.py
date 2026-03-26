def ft_tqdm(lst: range) -> None:  # type: ignore
    total = len(lst)
    for i, item in enumerate(lst, 1):
        progress = int(254 * i / total)
        bar = f"{'█' * progress}{' ' * (254 - progress)}"
        print(
            f"\r{int(progress/2.54)}%|{bar}| {i}/{total}", end="", flush=True
        )
        yield item
