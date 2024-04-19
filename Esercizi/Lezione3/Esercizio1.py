def change_vals_Whit_sum(d: dict[str, int]) -> dict[str, int]:
    print(f"il dizioario di input è {d}")
    somma = sum(list(d.valuse()))
    print(f"la somma è {somma}")
    out = {}
    for key in d:
        out[key] = d[key] / somma
        return out
    
def Rewrite_dict(d: dict[str, int]) -> dict[str, int]:









