import numpy as np
from typing import List

def print_latex(ws: List[np.ndarray], bs: List[np.ndarray]):
    print("\\begin{table}[H]")
    print("\t\\centering")

    for i in range(len(ws)):
        caption = f"Iteration: n = {i}, "
        if i == 0:
            print_latex_sub_table(ws[i],None,True,caption+"Weights")
            print_latex_sub_table(bs[i],None,False,caption+"Backtracking")
        else:
            print_latex_sub_table(ws[i],ws[i-1],True,caption+"Weights")
            print_latex_sub_table(bs[i],bs[i-1],False,caption+"Backtracking")
        if i == 4:
            print("\t\\caption{{Floyd-Warshall}}")
            print("\\end{table}")
            print("\\pagebreak")
            print("\\begin{table}[H]")
            print("\t\\ContinuedFloat")
            print("\t\\centering")

    print(f"\t\\caption{{Floyd-Warshall cont.}}")
    print(f"\t\label{{tab:Floyd-Warshall}}")
    print("\\end{table}")

def print_latex_sub_table(t: np.ndarray, t_prev: np.ndarray, weights: bool, caption: str):
    print("\t\t\\begin{subtable}{0.45\\textwidth}")
    print("\t\t\\centering")

    print_latex_tabular(t,t_prev,weights)

    print(f"\t\t\\caption{{{caption}}}")
    print(f"\t\t\label{{tab:{caption}}}")
    print("\t\t\\end{subtable}")

def print_latex_tabular(t: np.ndarray, t_prev: np.ndarray, weights):
    print("\t\t\t\\begin{tabular}[t]{c ? c | c | c | c | c | c }")
    print("\t\t\t & \\textbf{a} & \\textbf{b} & \\textbf{c} & \\textbf{d} & \\textbf{e} & \\textbf{f} \\\\")
    print("\t\t\t\specialrule{1pt}{0pt}{0pt}")
    rows = ["a","b","c","d","e","f"]
    for i in range(t.shape[0]):
        if i > 0:
            print("\t\t\t\\hline")
        print(f"\t\t\t\\textbf{{{rows[i]}}} ", end='')
        for j in range(t.shape[1]):
            if weights:
                if t[i,j] == np.Inf:
                    print("& ", end='')
                else:
                    if t_prev is not None and t[i,j] != t_prev[i,j]:
                        print(f"& \\textcolor{{red}}{{{int(t[i,j])}}} ", end='')
                    else:
                        print(f"& {int(t[i,j])} ", end='')
            else:
                if t[i,j] == np.Inf:
                    print("& ", end='')
                else:
                    if t_prev is not None and t[i,j] != t_prev[i,j]:
                        print(f"& \\textcolor{{red}}{{{rows[int(t[i,j])]}}} ", end='')
                    else:
                        print(f"& {rows[int(t[i,j])]} ", end='')
        print("\\\\")

    print("\t\t\t\\end{tabular}")


if __name__=="__main__":

    w = np.array(
        [np.array([np.Inf,1,2,np.Inf,np.Inf,np.Inf]),
        np.array([np.Inf,np.Inf,np.Inf,1,5,np.Inf]),
        np.array([np.Inf,2,1,2,3,np.Inf]),
        np.array([4,np.Inf,np.Inf,1,2,4]),
        np.array([np.Inf,np.Inf,np.Inf,np.Inf,10,2]),
        np.array([np.Inf,np.Inf,np.Inf,3,np.Inf,np.Inf])]
    )

    # b = np.array(
    #     [np.array([np.Inf,0,0,np.Inf,np.Inf,np.Inf]),
    #     np.array([np.Inf,np.Inf,np.Inf,1,1,np.Inf]),
    #     np.array([np.Inf,2,2,2,2,np.Inf]),
    #     np.array([3,np.Inf,np.Inf,3,3,3]),
    #     np.array([np.Inf,np.Inf,np.Inf,np.Inf,4,4]),
    #     np.array([np.Inf,np.Inf,np.Inf,5,np.Inf,np.Inf])]
    # )
    b = np.array([
        np.array([0,1,2,3,4,5]),
        np.array([0,1,2,3,4,5]),
        np.array([0,1,2,3,4,5]),
        np.array([0,1,2,3,4,5]),
        np.array([0,1,2,3,4,5]),
        np.array([0,1,2,3,4,5]),
    ])

    n = w.shape[0]

    ws = [np.copy(w)]
    bs = [np.copy(b)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if w[i,j] > w[i,k] + w[k,j]:
                    w[i,j] = w[i,k] + w[k,j]
                    b[i,j] = b[i,k]
        ws.append(np.copy(w))
        bs.append(np.copy(b))

    print_latex(ws,bs)
