---
layout: post
title:  "Representation Theory, Local Operators, and bound states of QCD"
date:   2021-11-30 
categories: physics
---

References: 
 - https://yufeizhao.com/research/youngtab-hcmr.pdf
 - Fulton and Harris

{::options toc_levels="1..3" /}
{:toc}

### 1) Introduction to Young Diagrams for representations of $$S_n$$

Let us start with a review of young diagrams and their uses for keeping track of representations. 

<def> A <i>partition</i> \(\lambda \vdash n\) of a number \(n \in \mathbb{Z}_{> 0}\) is a sequence of positive numbers \(\lambda_1 \geq \dots \geq \lambda_r\) with their sum equalling \(n\). We associate to every partition a <i>Young diagram</i> which is a left-aligned collection of boxes, with \(\lambda_i\) number of boxes in the \(i\)-th row. A <i>Young Tableau</i> is a young-diagram with the boxes labelled by the numbers \(\{1,\dots,n\}\). It is called <i>standard</i> if the numbers increase along the rows and along the columns.</def>

<def>Given a Young Diagram \(\lambda\), we can associate to it a permutation module (representation of \(S_n\)) called \(M_\lambda\). A basis is given by all (not necessarily standard) young tableaux of that diagram, modulo the relation where a young tableaux \(t_1^\lambda \sim t_2^\lambda\) if they have the same set of numbers in each row. We will denote the row-equivalency class of a Young Tableaux \(t^\lambda\) by \(\{t^\lambda\}\). In other words, the dimension is given by 
$$\text{dim } M_\lambda = \frac{n!}{\lambda_1!\lambda_2!\dots \lambda_r!}$$
\(S_n\) acts naturally by permuting where the numbers are in the tableaux.
</def>

<def>To each partition \(\lambda\) we can naturally associate an irreducible representation \(S_\lambda\) of \(S_n\); which will live inside the rep \(M_\lambda\) defined above. A basis is labelled by standard young-tableaux of shape \(\lambda\), under the map
$$ P : t^\lambda \mapsto \sum_{\pi \in C(t^\lambda)}\text{sign}(\pi) \{\pi(t)\}$$
where \(C(t^\lambda)\) is the subgroup of \(S_n\) that permutes just the numbers within each column of the tableaux \(t^\lambda\). This representation has dimension 
$$\text{dim} S_\lambda = \frac{n!}{h_1! h_2! \dots h_n!}$$
where \(h_i\) are the hook-length numbers for each of the boxes: the number of boxes to the right + the number of boxes below + 1 for the box itself. 
</def>

At this point, I've said too many words and drawn too few pictures; so here is an example picture for an irreducible representation of $$S_5$$:

![S5reps](/assets/reps5.jpeg)

Now at this point, I've shown too much without any proofs, so I'll waffle a bit about the backend. 

<lem>\(S_\lambda\) as defined above actually forms a sub-representation of \(M_\lambda\).</lem>
<proof>We need to check that the action of \(S_n\) on \(M_n\) preserves the \(S_\lambda\) subspace. By definition, \(S_\lambda\) is spanned by \(P(t^\lambda)\) for \(t^\lambda\) standard
$$P : t^\lambda \mapsto \sum_{\pi \in C(t^\lambda)}\text{sign}(\pi) \{\pi(t^\lambda)\}$$
but note that \(P(t^\lambda)\) for nonstandard tableaux also lives in \(S_\lambda\). A funny fact is that \(P\) and \(\sigma\) commute:
$$P(\sigma(t)) = \sum_{\pi \in C(\sigma(t^\lambda))} \text{sign}(\pi) \{\pi(\sigma(t^\lambda))\} =  \sum_{\pi' \in C(t^\lambda)} \text{sign}(\sigma \pi' \sigma^{-1}) \{\sigma \pi' \sigma^{-1} \sigma (t^\lambda)\}$$
$$ =  \sum_{\pi \in C(t^\lambda)} \text{sign}(\pi) \{\sigma(\pi(t^\lambda))\} = \sigma(P(t))$$
Since \(\sigma(P(t^\lambda)) = P(\sigma(t^\lambda))\), then the action preserves \(S_\lambda\). 
</proof>

<lem>\(S_\lambda\)'s dimension is indeed given by the formula in terms of the hook-lengths
$$\text{dim} S_\lambda = \frac{n!}{h_1! h_2! \dots h_n!}$$</lem>
<proof>If we take as fact that \(S_\lambda\) has basis labelled by standard tableaux, then we just need to count the standard tableaux. \(n!\) gives the total number of ways of writing numbers into the boxes, but the top-left box has the requirement that it is the smallest number out of the hook it generates, so we must divide by \(h_1!\), similarly for all the other boxes. </proof>

### 2) Young Diagrams for $$SU(N)$$

So we can now draw some diagrams for irreps of $$S_n$$, let's move onto the case of $$SU(N)$$ now. To start, let's recall a little about how the weight-diagrammatic classification of irreps works for lie algebras, following the steps in Fulton and Harris. 

 - Step 1 : Find an  abelian subalgebra (the <i>Cartan Subalgebra</i>) $$\mathfrak{h} \subset \mathfrak{g}$$ which acts (via the adjoint map) diagonally on $$\mathfrak{g}$$. In practice, this is the subalgebra of diagonal matrices. 
 - Step 2 : Decompose $$\mathfrak{g} = \mathfrak{h} \oplus \left(\bigoplus_\alpha \mathfrak{g}_\alpha\right)$$, where $$\alpha \in \mathfrak{h}^*$$ describes the Cartan Subalgebra's adjoint action on the necessarily one-dimensional subspace $$\mathfrak{g}_\alpha$$. These $$\alpha$$ are called roots. In general, a representation will split as a direct sum $$V = \bigoplus_\alpha V_\alpha$$ where $$\mathfrak{h}$$ acts diagonally, the $$\alpha$$ are called the weights of the representation.  The lie algebra elements $$X_\beta$$ corresponding to roots $$\beta$$ act by $$X_\beta : V_\alpha \to V_{\alpha + \beta}$$ by the fundamental calculation:

 $$h_i(X_\beta(v_\alpha)) = X_\beta(h_i(v_\alpha)) + [h_i,X_\beta] v_\alpha = (\alpha_i + \beta_i) X_\beta v_\alpha$$

 - Step 3 : The <i>Killing Form</i> $$\langle X,Y \rangle_\text{Killing} = \text{Tr}(X_\text{Ad} Y_\text{Ad})$$ gives us an inner product on $$\mathfrak{g}$$, which in turn provides us an isomorphism $$\mathfrak{g} \simeq \mathfrak{g}^*$$. We can choose an orthonormal basis of $$\mathfrak{h}^*$$ with respect to this Killing Form, on which we can plot the roots, and the lattice of integer combinations that they generate. Weights of arbitrary representations will live on this root lattice. 
 - Step 4 : Choose some irrational hyperplane in $$\mathfrak{h}^*$$ (in the sense that it doesn't intersect any root lattice points), and call the roots on one side <i>positive</i>, the other side <i>negative</i>. The roots will naturally be paired up as $$\alpha, -\alpha$$. 
 - Step 5 : There is a symmetry group called the Weyl group that acts on our root lattice; which is generated by reflections about the hyperplanes that each root defines (the hyperplane perpendicular to the root, under the Killing form). For any collection of weights corresponding to a representation, they will be symmetric under the action of the Weyl group, so to simplify the discussion we choose a particular <i>Weyl chamber</i> of roots where the symmetry pushes the chamber around to fill out the whole root lattice. In particular, if we have a choice of positive roots $$\alpha_i^+$$ then we naturally choose the Weyl chamber to consist of the weights $$\beta$$ such that $$\langle \alpha_i^+,\beta\rangle \geq 0$$. Then, weights in the weyl chamber are in bijection with irreducible representations of $$\mathfrak{g}$$. 

<warn>Many technical things were skipped over; should read Fulton and Harris chapter 14 for the full picture. There should also be a picture of the weight diagrams included here: but I had to return my ipad at the end of the semester so I can't draw one anymore teehee. So, prepare for the post to get a lot more scuffed</warn>

This general picture is however rather complicated and geometrical. It turns out in the case of $$SU(N)$$ that there are simple rules we can write down that handle all of this root-lattice geometry for us, and let us get to actual computations. The irreps of $$SU(N)$$ will be associated once again to young diagrams, this time of any horizontal size; under the constraint that the columns do not exceed $$N$$ height (if they are $$N$$ height, you can cross them out as they correspond to a singlet representation). The dimension of the irrep is found by placing an $$N$$ in the top-left box, then as you go to the right you add one, and as you go down you subtract one. Multiply all these numbers, and divide by the product of the hook-lengths (the dimension of the corresponding irrep of $$S_\text{# of boxes}$$). For example the irrep corresponding to the partition $$(3,2,1)$$ has dimension:

$$\begin{array}{cccc}
- & - & - & - \\
| & N & N+1 & N+2 \\
| & N-1 & N &  \\
| & N-2 &  &  \end{array} \quad \bigg/ \quad \begin{array}{cccc}
| & 5 & 3 & 1 \\
| & 3 & 1 &  \\
| & 1 &  &  \end{array} = \frac{N^2(N^2-1)(N^2-4)}{45}$$

which is $$64$$ when $$N = 4$$. 