from math import sqrt

def mean(lst):
    return sum(lst)/len(lst)

def median(lst, l):
    if (l % 2 != 0):
        return lst[int(l / 2)]
    else:
        return sum(lst[(int(l / 2)) - 1:(int(l / 2)) + 1])/2

def ft_statistics(*args: any, **kwargs: any) -> None:
    for k, val in kwargs.items():
        if len(args) == 0:
            print("ERROR")
        elif val == "mean":
            m = mean(args)
            print(f"mean : {m}")
        elif val == "median":
            sorted_args = sorted(args)
            l = int(len(sorted_args))
            M = median(sorted_args, l)
            print(f"{val} : {M}")
        elif val == "quartile":
            quartile = [0, 0]
            s1 = sorted_args[:int(l/2)]
            s2 = sorted_args[int(l/2):]
            quartile[0] = float(s1[int(len(s1)/2)])
            quartile[1] = float(s2[int(len(s1)/2)])
            print(f"{val} : {quartile}")
        
        
        
        elif val == "std":
            m = mean(args)
            std = 0
            for n in args:
                std += (n - m)**2
            std = sqrt(std/len(args))
            print(f"std : {std}")
        elif val == "var":
            m = mean(args)
            var = 0
            for n in args:
                var += (n - m)**2
            var = var/len(args)
            print(f"var : {var}")