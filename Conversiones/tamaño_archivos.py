# --- Base 10 ---
def bytes_a_kb(b): return b / 1000   
def kb_a_bytes(kb): return kb * 1000
def kb_a_mb(kb): return kb / 1000
def mb_a_kb(mb): return mb * 1000
def mb_a_gb(mb): return mb / 1000
def gb_a_mb(gb): return gb * 1000  
def gb_a_tb(gb): return gb / 1000
def tb_a_gb(tb): return tb * 1000
def kb_a_gb(kb): return kb / 1_000_000
def gb_a_kb(gb): return gb * 1_000_000
def mb_a_tb(mb): return mb / 1_000_00
def tb_a_mb(tb): return tb * 1_000_000
def kb_a_tb(kb): return kb / 1_000_000_000
def tb_a_kb(tb): return tb * 1_000_000_000
def bytes_a_mb(b): return b / 1_000_000
def mb_a_bytes(mb): return mb * 1_000_000
def bytes_a_gb(b): return b / 1_000_000_000
def gb_a_bytes(gb): return gb * 1_000_000_000
def bytes_a_tb(b): return b / 1_000_000_000_000
def tb_a_bytes(tb): return tb * 1_000_000_000_000

# --- Base 2 ---
def bytes_a_kib(b): return b / 1024
def kib_a_bytes(kib): return kib * 1024
def kib_a_mib(kib): return kib / 1024
def mib_a_kib(mib): return mib * 1024
def mib_a_gib(mib): return mib / 1024
def gib_a_mib(gib): return gib * 1024
def gib_a_tib(gib): return gib / 1024
def tib_a_gib(tib): return tib * 1024
def kib_a_gib(kib): return kib / (1024**2)
def gib_a_kib(gib): return gib * (1024**2)
def mib_a_tib(mib): return mib / (1024**2)
def tib_a_mib(tib): return tib * (1024**2)
def kib_a_tib(kib): return kib / (1024**3)
def tib_a_kib(tib): return tib * (1024**3)
def bytes_a_mib(bytes): return bytes / (1024 ** 2)
def mib_a_bytes(mib): return mib * (1024 ** 2)
def bytes_a_gib(bytes): return bytes / (1024 ** 3)
def gib_a_bytes(gib): return gib * (1024 ** 3)
def bytes_a_tib(bytes): return bytes / (1024 ** 4)
def tib_a_bytes(tib): return tib * (1024 ** 4)

# --- Cruzadas entre base 10 y base 2 ---
def kb_a_kib(kb): return (kb * 1000) / 1024
def kib_a_kb(kib): return (kib * 1024) / 1000
def mb_a_mib(mb): return (mb * 1000**2) / 1024**2
def mib_a_mb(mib): return (mib * 1024**2) / 1000**2
def gb_a_gib(gb): return (gb * 1000**3) / 1024**3
def gib_a_gb(gib): return (gib * 1024**3) / 1000**3
def tb_a_tib(tb): return (tb * 1000**4) / 1024**4
def tib_a_tb(tib): return (tib * 1024**4) / 1000**4