# sparse-param-budget

[Interactive original](../upstream/app/public/viz/index.html?c=sparse-param-budget) · [Poster](../upstream/app/public/viz/posters/sparse-param-budget.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/sparse-param-budget-CHMXyNqI.js)

## Controls

```json
{}
```

Animation duration: 10.700000000000001 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 17× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

2.974

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 17× active, 31% tables

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

0.010 below more experts

Both rows hold the same parameters at about the same compute.

Each square is 280M parameters, the active set: the top row spends the rest on more experts, the bottom row stops the expert pool at 12× or 4× and gives the rest to n-gram tables.

Both rows hold the same parameters at about the same compute.

## Sample 2

Parameters: `{"t": 5.3500000000000005}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 23× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

2.949

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 23× active, 48% tables

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

0.006 above more experts

Both rows hold the same parameters at about the same compute.

Once tables hold more than about 40% of the parameters, more experts win again.

Both rows hold the same parameters at about the same compute.

## Sample 3

Parameters: `{"t": 10.700000000000001}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 17× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

2.974

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 17× active, 31% tables

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

0.010 below more experts

Both rows hold the same parameters at about the same compute.

Tables pay only once the expert pool is already large: added to the 4× pool, they lose from the start. Where extra parameters do most depends on the experts you already have.

Both rows hold the same parameters at about the same compute.

## Sample 4

Parameters: `{"t": 1.5}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 12× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

3.007

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 12× active, no tables yet

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

Both rows hold the same parameters at about the same compute.

Right after the pool stops at 12×, tables lower the loss more than the same parameters spent on experts.

Both rows hold the same parameters at about the same compute.

## Sample 5

Parameters: `{"t": 4.7}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 23× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 23× active, 48% tables

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

Both rows hold the same parameters at about the same compute.

Once tables hold more than about 40% of the parameters, more experts win again.

Both rows hold the same parameters at about the same compute.

## Sample 6

Parameters: `{"t": 8}`

More experts or n-gram embeddings: which lowers loss more for the same parameters?

More routed experts

the pool grows, active parameters fixed (LongCat’s runs, 280M active, 300B tokens; Kimi K2 ships 384 experts at top-8)

activeexpertsn-gram tables

total 17× active

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

Hashed n-gram embedding tables

the expert pool stops growing and tables take the rest, same total and active parameters as the row above (LongCat; LongCat-Flash-Lite ships 31B of its 69B as tables)

total 17× active, 31% tables

English validation loss

2.90

3.00

3.10

4×

12×

20×

30×

44×

total parameters, as a multiple of the 280M active

more experts

experts stop at 4×, then tables

experts stop at 12×, then tables

Both rows hold the same parameters at about the same compute.

Tables pay only once the expert pool is already large: added to the 4× pool, they lose from the start. Where extra parameters do most depends on the experts you already have.

Both rows hold the same parameters at about the same compute.
