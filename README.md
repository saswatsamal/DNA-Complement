# DNA Complement

<img src="https://github.com/saswatsamal/DNA-Complement/blob/main/img/DNA%20Complement.png">

<h3> What is DNA Complementary Base Paring? 🧬 </h3>

<p>Complementary base pairing is the phenomenon where in DNA guanine always hydrogen bonds to cytosine and adenine always binds to thymine.
The bond between guanine and cytosine shares three hydrogen bonds compared to the A-T bond which always shares two hydrogen bonds.</p>

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Complementarity_%28DNA%29.png/250px-Complementarity_%28DNA%29.png">

<h4> What Bioinformatics tells about it? 💻 </h4>

<p>Complementarity allows information found in DNA or RNA to be stored in a single strand. The complementing strand can be determined from the template and vice versa as in cDNA libraries. This also allows for analysis, like comparing the sequences of two different species. Shorthands have been developed for writing down sequences when there are mismatches (ambiguity codes) or to speed up how to read the opposite sequence in the complement (ambigrams).</p>


<h3> What my program does? 👩‍💻</h3>

- Fiding the reverse and complement of the DNA/RNA sequences are usually tiring, specially when the sequecnes are too long.
- To solve this tiring work, I've designed the code taking help from others. It will simply take the sequence as input and will give the reverse and complement as output.
- Also at the last, it does show the IUPAC Degeneracy Table of all the bases and their complementary.



<h3> How to execute it? ▶</h3>

- Clone the repository to your system.
  - Learn how to clone [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
- Execute the program by running `run.py`

```
python -u "run.py"
```

- Enter the DNA/RNA Sequence and hit enter.

```
Enter: ATCGCCAATTGGCAATT
↵
```

- You have now successfully executed your code.

<h4> Output 📤</h4>

```
Enter: ATCGCCAATTGGCAATT
Reverse: AATTGCCAATTGGCGAT
ATCGCCAATTGGCAATT
|||||||||||||||||
TAGCGGTTAACCGTTAA

The IUPAC Degeneracies Table
+------+-------------------+-------------------+--------------------+
| Base |        Name       | Bases Represented | Complementary Base |
+------+-------------------+-------------------+--------------------+
|  A   |      Adenine      |         A         |         T          |
|  T   |     Thymidine     |         T         |         A          |
|  U   | Uridine(RNA only) |         U         |         A          |
|  G   |     Guanidine     |         G         |         C          |
|  C   |      Cytidine     |         C         |         G          |
|  Y   |     pYrimidine    |        C T        |         R          |
|  R   |       puRine      |        A G        |         Y          |
|  S   |  Strong(3Hbonds)  |        G C        |         S*         |
|  W   |   Weak(2Hbonds)   |        A T        |         W*         |
|  K   |        Keto       |       T/U G       |         M          |
|  M   |       aMino       |        A C        |         K          |
|  B   |       not A       |       C G T       |         V          |
|  D   |       not C       |       A G T       |         H          |
|  H   |       not G       |       A C T       |         D          |
|  V   |      not T/U      |       A C G       |         B          |
|  N   |      Unknown      |      A C G T      |         N          |
+------+-------------------+-------------------+--------------------+
```
<h3> What more? 🤔💭</h3>

- To reomve some bugs!
  - You found one? Then why don't you inform me but citing an issue [here](https://github.com/saswatsamal/DNA-Complement/issues/new?assignees=&labels=&template=other-issue.md&title=)

- To make this program into GUI based.

- To make webpage interface.

<h3> References 🔗</h3>

1. [Complementarity (molecular biology).](https://en.wikipedia.org/wiki/Complementarity_(molecular_biology))

2. [Reverse and/or complement DNA sequences](http://arep.med.harvard.edu/labgc/adnan/projects/Utilities/revcomp.html)

