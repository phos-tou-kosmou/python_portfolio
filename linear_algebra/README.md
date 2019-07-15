# Linear Algebra Portfolio

    The main idea for this folder is to understand pythonic implementation for the underlying math for linear algebra.

    Future additions:
        Hessenberg Deflations
        QR Algorithms
        Gauss Seidel Method

### How to review

    first:
       
        $ git clone https://github.com/phos-tou-kosmou/linear_algebra
       

    next: 
      
       $ chmod +x transposition
       
       
       $ python3 ./transposition
       

    There should be a default function being tested while running the script;
    however, it is a small library implementation so import it and test out the functions

Note:
    Need to include tests and implement multithreading
    
# Notes on matrix_transposition

### 1
06/07/2019  4:45 PM
The algorithm below is used to determine the efficient multiplication of two matrices.  As one can see result[0] is the
correct computation for Ax = x*y in the index A[0][0].  The same goes for result[1] as well.  I have determined
the issue deals with lack of computation with the inner product space, which is viewed more deeply within Hessenberg deflations
and QR algorithms.  My next decision would be to implement a while loop to iterate over each list and change from ranges to
enumeration of one np.array made into a list.

```
result = np.array([0, 0, 0, 0]) 
for i in range(0, 2): 
  for j in range(0, 2): 
    result[i] += listx[i][j]*listy[j][i] 
 
result 
array([19, 50,  0,  0]) 
```
### 2
06/07/2019 11:30PM
Even though this algorithm more "hardcoded" than I would like, it is providing feedback that will allow me to complete
my inner product space (i.e. result[1] & result[2]).  I am now thinking the approach of finding eigenvalues first
might be a better.  The main reason being that an eigenvector can be valuable later on, when computing additional
algorithms.  However, I really just want to see it work before optimization.

```
for i in range(0,2): 
  while p != 4: 
    for j in range(0,2): 
      result[p] += listx[i][j] * listy[j][k] 
    p = p + 1 
    k = 1 
  k = 0 
 
result 
array([19, 22, 0, 0])
```

The consensus is a "for in for in while" is nessecary for matrix multiplication.  The mistake I was making was that I needed an index variable for the collection array and an additional loop needed for the 3D variable.  Even though it is a 2 dimensional structure there is a dependency upon a third variable to iterate the rows for j.  View transposition.py for the implementation details.
