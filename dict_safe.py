class SafeDict(dict):
    def safe_get(self, dot_separated_attributes, default=None):
        attribute = dot_separated_attributes.split(".")
        val = self
        for a in attribute:
            if a not in val:
                return default
            if isinstance(val, dict):
                val = val.get(a, None)
                if val is None:
                    return default
        return val


d = SafeDict(s="a string", d={"name": "a dict"})
print d.safe_get("s", "")
print d.safe_get("d", {})
print d.safe_get("d.name", "")
print d.safe_get("d.name.foo", "unknown yet but doesn't harm")
