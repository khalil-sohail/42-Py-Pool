import time
from datetime import date

t = time.time()

print(
    f"Seconds since January 1, 1970: {format(t, ',.4f')} or "
    f"{t:.2e} in scientific notation\n"
    f"{date.today().strftime('%b %d %Y')}"
)
