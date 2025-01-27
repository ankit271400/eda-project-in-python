from typing import Any, Generator, Literal
from typing_extensions import Self

from sympy.combinatorics.perm_groups import Coset
from sympy.core.basic import Atom
from sympy.core.expr import Expr
from sympy.core.numbers import Integer

class Cycle(dict):
    def __missing__(self, arg) -> int: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __call__(self, *other) -> Cycle: ...
    def list(self, size=...) -> list[Any]: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __init__(self, *args) -> None: ...
    @property
    def size(self) -> Literal[0]: ...
    def copy(self) -> Cycle: ...

class Permutation(Atom):
    is_Permutation = ...
    _array_form = ...
    _cyclic_form = ...
    _cycle_structure = ...
    _size = ...
    _rank = ...
    def __new__(cls, *args, size=..., **kwargs): ...
    @property
    def array_form(self): ...
    def list(self, size=...): ...
    @property
    def cyclic_form(self) -> list[Any]: ...
    @property
    def full_cyclic_form(self) -> list[Any]: ...
    @property
    def size(self) -> None: ...
    def support(self) -> list[int]: ...
    def __add__(self, other) -> Self: ...
    def __sub__(self, other) -> Self: ...
    @staticmethod
    def rmul(*args): ...
    @classmethod
    def rmul_with_af(cls, *args) -> Self: ...
    def mul_inv(self, other) -> Self: ...
    def __rmul__(self, other) -> Coset | Self: ...
    def __mul__(self, other) -> Coset | Self: ...
    def commutes_with(self, other) -> bool: ...
    def __pow__(self, n) -> Self: ...
    def __rxor__(self, i) -> list[Any] | Coset | Permutation: ...
    def __xor__(self, h) -> Self: ...
    def transpositions(self) -> list[Any]: ...
    @classmethod
    def from_sequence(cls, i, key=...) -> Permutation: ...
    def __invert__(self) -> Self: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __repr__(self): ...
    def __call__(self, *i) -> list[Any] | Coset | Self: ...
    def atoms(self) -> set[Any]: ...
    def apply(self, i) -> Integer | AppliedPermutation: ...
    def next_lex(self) -> Self | None: ...
    @classmethod
    def unrank_nonlex(cls, n, r) -> Self: ...
    def rank_nonlex(self, inv_perm=...) -> Literal[0]: ...
    def next_nonlex(self) -> Self | None: ...
    def rank(self) -> int: ...
    @property
    def cardinality(self) -> int: ...
    def parity(self) -> int: ...
    @property
    def is_even(self) -> bool: ...
    @property
    def is_odd(self) -> bool: ...
    @property
    def is_Singleton(self) -> bool: ...
    @property
    def is_Empty(self) -> bool: ...
    @property
    def is_identity(self) -> bool: ...
    @property
    def is_Identity(self) -> bool: ...
    def ascents(self) -> list[int]: ...
    def descents(self) -> list[int]: ...
    def max(self) -> Literal[0]: ...
    def min(self) -> int: ...
    def inversions(self) -> int: ...
    def commutator(self, x) -> Self: ...
    def signature(self) -> Literal[1, -1]: ...
    def order(self) -> Any: ...
    def length(self) -> int: ...
    @property
    def cycle_structure(self) -> dict[Any, int]: ...
    @property
    def cycles(self) -> int: ...
    def index(self) -> int: ...
    def runs(self) -> list[Any]: ...
    def inversion_vector(self) -> list[int]: ...
    def rank_trotterjohnson(self) -> int: ...
    @classmethod
    def unrank_trotterjohnson(cls, size, rank) -> Self: ...
    def next_trotterjohnson(self) -> Self | None: ...
    def get_precedence_matrix(self): ...
    def get_precedence_distance(self, other): ...
    def get_adjacency_matrix(self): ...
    def get_adjacency_distance(self, other): ...
    def get_positional_distance(self, other) -> int: ...
    @classmethod
    def josephus(cls, m, n, s=...) -> Self: ...
    @classmethod
    def from_inversion_vector(cls, inversion) -> Self: ...
    @classmethod
    def random(cls, n) -> Self: ...
    @classmethod
    def unrank_lex(cls, size, rank) -> Self: ...
    def resize(self, n) -> Permutation | Self: ...

    print_cyclic = ...

Perm = Permutation
_af_new = ...

class AppliedPermutation(Expr):
    def __new__(cls, perm, x, evaluate=...) -> Self: ...
