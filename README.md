# Algorithms

## 


\usepackage{amsmath}
\usepackage{algorithm}
\usepackage{algpseudocode}

\begin{algorithm}
\caption{5-Fold Cross-Validation for XGBoost Model Accuracy}
\begin{algorithmic}[1]
\Require Dataset $D$, Xgboost algorithm Model $Xgb$
\Ensure Accuracy per fold $Acc_i$
\State Split $D$ into 5 equal parts: $D_1, D_2, D_3, D_4, D_5$
\For{$i \gets 1$ to $5$}
    \State $D_{\text{train}} \gets D \setminus D_i$
    \State $D_{\text{test}} \gets D_i$
    \State $M \gets Xgb(D_{\text{train}})$
    \State $Acc_i \gets \text{Accuracy}(M, D_{\text{test}})$
\EndFor
\State \Return $Acc_i$
\end{algorithmic}
\end{algorithm}

```latex
\documentclass{article}
\usepackage{algorithm}
\usepackage{algpseudocode}
\begin{document}

\begin{algorithm}
\caption{Euclid’s algorithm}\label{euclid}
\begin{algorithmic}[1]
\Procedure{Euclid}{$a,b$}\Comment{The g.c.d. of a and b}
\While{$b\neq0$}\Comment{We have the answer if b is 0}
\State $t \gets b$
\State $b \gets a\bmod b$
\State $a \gets t$
\EndWhile
\State \textbf{return} $a$\Comment{The gcd is a}
\EndProcedure
\end{algorithmic}
\end{algorithm}

\end{document}