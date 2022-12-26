# ComputeBoundsForAnyEquation
Consider a certain algorithm whose complexity is given by the following recurrence 𝑇(𝑛 + 1) = 𝑇(𝑛)( (𝑛2 + 4𝑛)/(𝑛2 + 4𝑛 + 3))^𝑛 (𝑛+4)/(𝑛+1) with the initial condition T(1)=4. with the initial condition T(1)=4. Find the asymptotic complexity of T(n) by investigating numerical results of this recurrence

In order to approach to the solution of this recurrence equation we have employed a solution that gradually approaches to to the desired answer by asumming different values to the upper bound and the lower bound and then comparing this graph with the graph of the given equation, Hence reaching the desired solution

Upper Bound Analysis:
For g(n) = n:
From Graph 1 we observe that the upper bound is satisfied by O(n). Graph-1:
  
  From the above graph, we see that the upper bound condition is true for all n0 = 16 and c2= 1.
For g(n) = n1/8
The upper bound can be reduced by decreasing the power of n. Therefore, O(n1/8) has a tighter Upper bound than O(n) and Graph 2 will be the output of it. Graph-2:
As seen from graph 2, n0= 226.5 and c2= 10.
For g(n)=n1/16
For complexity O(n1/16) the upper bound condition is true for all n0= 226.5 and c2= 10 as shown in Graph 3.
Graph-3:
 
  For g(n) = n1/∞
From previous observations we can conclude that the lesser the power of n, more closer the upper bound gets to the original function. Therefore, O(n1/∞) which is equivalent to O(1) is the best possible upper bound.
Graph-4:
Lower Bound Analysis:
Similar to upper bound analysis, we can do the lower bound analysis
For g(n) = n1/8
By changing the coefficient, we can find the lower bound of the function g(n) as shown in Graph-5.
Graph – 5:
  
  However, at very large values of n, the lower bound line will intersect the function T(n). Hence, we could not find the minimum value of n0, after which the orange line stays below the blue line. This contradicts the definition of the lower bound, and hence cannot be the solution. This can be seen more clearly if we increase the g(n)’s coefficient as shown in Graph-6.
Graph -6:
From the above figure, it can be observed that the g(n) intersects f(n) at n0 ≈ 1500, and it does not satisfy the lower bound criteria.
For g(n)=n1/16
Similarly, for n1/16, the lower bound intersects at n ≈ 4000 and we cannot find n0, after which the lower bound stays below the T(n) function
Graph-7:
 
 For g(n) = n1/∞
From previous observations, it is clear that the g(n) as lower bound will only suffice, when its slope is 0 and is parallel to the T(n) function. Hence, g(n) = 1 satisfies the lower bound condition and we can find the n0 after which the g(n) stays lower than the T(n).
Graph-8:
From Graph 4 and Graph 8, we can conclude that the T(n) function has an asymptotic complexity of Θ(1).

