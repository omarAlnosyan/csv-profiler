class ColumnProfile:
    def __init__(self, name: str, inferred_type: str, total: int, missing: int, unique: int):
        self._name = name
        self._inferred_type = inferred_type
        self._total = total
        self._missing = missing
        self._unique = unique

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @property
    def inferred_type(self) -> str:
        return self._inferred_type

    @inferred_type.setter
    def inferred_type(self, value: str) -> None:
        self._inferred_type = value

    @property
    def total(self) -> int:
        return self._total

    @total.setter
    def total(self, value: int) -> None:
        self._total = value

    @property
    def missing(self) -> int:
        return self._missing

    @missing.setter
    def missing(self, value: int) -> None:
        self._missing = value

    @property
    def unique(self) -> int:
        return self._unique

    @unique.setter
    def unique(self, value: int) -> None:
        self._unique = value

    @property
    def missing_pct(self) -> float:
        return 0.0 if self._total == 0 else 100.0 * self._missing / self._total
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "type": self.inferred_type,
            "total": self.total,
            "missing": self.missing,
            "missing_pct": self.missing_pct,
            "unique": self.unique,
        }

    def __repr__(self) -> str:
        return (
            f"ColumnProfile(name={self.name!r}, type={self.inferred_type!r}, "
            f"missing={self.missing}, total={self.total}, unique={self.unique})"
        )
