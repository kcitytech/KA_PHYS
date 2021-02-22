# KA_PHYS: PHYS 4100/4150

python3 should be used to run scripts to avoid issues with special characters in comments.

## PHYS 4150

### BallDrop.py
```
python3 BallDrop.py
Exercise 2.1 - Ball Drop
Height of ball (meters):100
The ball will take approximately 4.5152 seconds to hit the ground.
```
```
python3 BallDrop.py --height 100
Exercise 2.1 - Ball Drop
The ball will take approximately 4.5152 seconds to hit the ground.
```

### RelativisticSpaceship.py
```
python3 RelativisticSpaceship.py
Exercise 2.4 - Spaceship
Distance (light years):10
Speed (Decimal fraction speed of light):.99
The observer on earth expects the spaceship to reach its target in ~10.101 years.
The observer on the spaceship perceives ~1.4249 years elapsing before reaching the planet.
```
```
python3 RelativisticSpaceship.py --distance 10 --speed 0.99
Exercise 2.4 - Spaceship
The observer on earth expects the spaceship to reach its target in ~10.101 years.
The observer on the spaceship perceives ~1.4249 years elapsing before reaching the planet.
```

#### CurvePlotting.py
```
python3 CurvePlotting.py
```

![CurvePlotting](Output/CurvePlotting.png)

#### CalculatingDerivatives.py
```
python3 CalculatingDerivatives.py 
Example 4.3

Derivative at x = 1 delta = 0.01: (truncated)

	Approximation: 1.010000
	Actual Stored: 1.000000

NOTE: Expect approximation to differ significantly with large delta. Reducing delta will result in improved accuracy until a point at which error will compound due to machine precision.

Graphs displayed show as delta decreases error will correspondingly decrease. 
    When delta becomes to small error will increase due to accumulation of errors due to machine precision.
```
```
python3 CalculatingDerivatives.py --x 2 --delta 0.0001
Example 4.3

Derivative at x = 2.0 delta = 0.0001: (truncated)

	Approximation: 3.000100
	Actual Stored: 3.000000

NOTE: Expect approximation to differ significantly with large delta. Reducing delta will result in improved accuracy until a point at which error will compound due to machine precision.

Graphs displayed show as delta decreases error will correspondingly decrease. 
    When delta becomes to small error will increase due to accumulation of errors due to machine precision.
```

![DeltasSpecific](Output/DeltasSpecific.png)
![DeltasRange](Output/DeltasRange.png)

## PHYS 4100

### BallDropTime.py
```
python3 BallDropTime.py 
Example 2.1
Height of tower (meters):10
  Time Elapsed (seconds):1
The ball is ~5.095 meters above the ground.
```

### Catalan.py
```
python3 Catalan.py
Catalan(n):20
6564120420
```

### NumpyArrays.py
```
python3 NumpyArrays.py 
[3. 3. 3. 3.]
[1.         1.33333333 1.5        1.6       ]
[1 1 1 1]
```

### MachinePrecision.py
```
python3 MachinePrecision.py 
2.220446049250313e-16
```

### Float.py
```
python3 Float.py
<class 'float'>
        0.10000000000000000555
```

### Difference.py
```
python3 Difference.py
1.4210854715202004
1.4142135623730951
```

### Quadratic.py
```
python3 Quadratic.py
Solution for a=0.001, b=1000, c=0.001:
Roots-Standard Formula:  -999999.999999 -9.99989424599e-07
Roots-Alternate Formula: -1000010.57551 -1e-06
Roots-Numpy:             -999999.999999 -1e-06
a:1
b:-8
c:12
Roots-Standard Formula:  2.0 6.0
Roots-Alternate Formula: 2.0 6.0
Roots-Numpy:             2.0 6.0
```

```
python3 Quadratic.py
Solution for a=0.001, b=1000, c=0.001:
Roots-Standard Formula:  -999999.999999 -9.99989424599e-07
Roots-Alternate Formula: -1000010.57551 -1e-06
Roots-Numpy:             -999999.999999 -1e-06
a:1
b:4
c:5
Roots-Standard Formula:  (-2+1j) (-2-1j)
Roots-Alternate Formula: (-2-1j) (-2+1j)
Roots-Numpy:             (-2+1j) (-2-1j)
```

### Integration.py
```
python3 Integration.py 
Trapezoidal method = 4.50656            (  10 slices)
Trapezoidal method = 4.401066656        ( 100 slices)
Trapezoidal method = 4.4000106666656    (1000 slices)
  Simpson's method = 4.400426666666667  (  10 slices)
  Simpson's method = 4.400000042666668  ( 100 slices)
  Simpson's method = 4.400000000004266  (1000 slices)
Simpson's Error <    0.00002666666666666373
```

### QuantumHarmonicOscillator.py
```
time python3 QuantumHarmonicOscillator.py 
Average Energy = 99.9554313409348 (1000 iterations)
Average Energy = 100.000833331944 (1000000 iterations)
Average Energy = 99.0107219866263 (1000000000 iterations)

real	15m2.296s
user	0m34.584s
sys	1m27.088s
```

### Gaussian.py
```
python3 Gaussian.py 
Value: 4.400000000000037
```

### CentralDifference.py
```
python3 CentralDifference.py
```
![CentralDifference](Output/CentralDifference.png)