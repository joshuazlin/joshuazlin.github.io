---
layout: post
title:  "Spontaneous Symmetry Breaking"
date:   2021-11-30 
categories: physics
---

Spontaneous symmetry breaking occurs whenever a system's ground state does not respect the symmetries that the system itself does. 

1. [Example 1 : ](#Example 1)

## Example 1 : $$\mathbb{Z}_2$$ symmetry

The classical Ising model is a canonical example of $$\mathbb{Z}_2$$ symmetry breaking. Taking a look at the Hamiltonian:

$$H = -J \sum_{\langle i, j \rangle} \sigma_i \sigma_j, \quad J > 0, \sigma_i \in \{ +1,-1\}$$

where we sum over all neighboring pairs of spins $$\langle i,j\rangle$$. Notice that there is a symmetry given by $\sigma \mapsto -\sigma$, but in the ground state the system must 'pick out' one of the two possible choices; either to have all the spins pointing up, or all the spins pointing down. In the case where you are in more than one dimension, you even have a phase transition at some critical temperature $$T_c$$, where below this critical temperature you see the system exhibit spontaneous magnetization. Another feature that we can imagine about discrete spontaneous symmetry breaking is the appearance of *domain walls*. If we were to take a system thermalized at some temperature $$T > T_c$$ and then rapidly cool it below $$T_c$$, it won't have time to thermalize and you will have pockets in space that choose different ground states (here, all spins pointing up or all spins pointing down); between these regions are domain walls. 

If we wanted to complicate matters, we can talk about real $$\phi^4$$ theory:

$$\mathcal{L} = \frac{1}{2}\partial_\mu \phi \partial^\mu \phi - m^2 \phi^2 - \frac{\lambda}{4!} \phi^4$$

which is once again symmetric under $\phi \to -\phi$, and the classical extrema take values at $$\phi =$$ 




