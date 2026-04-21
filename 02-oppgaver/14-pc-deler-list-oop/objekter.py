# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2026-04-14 00:13:51
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2026-04-14 00:19:38

from prosessor import Prosessor
from grafikkort import Grafikkort
from ram import Ram
from lagring import Lagring
from hovedkort import Hovedkort
from psu import Psu
from kjoeling import Kjoeling
from kabinett import Kabinett
from nettverkskort import Nettverkskort
from lydkort import Lydkort

from vifte import Vifte

# ============================================================
# OBJEKTER - 2 per klasse
# ============================================================

cpu1 = Prosessor(
    "Intel",
    "Core i9-13900K",
    2000,
    5500,
    "god",
    24,
    32,
    3.0,
    5.8,
    36,
    "LGA1700",
    125,
    "Ja - Intel UHD 770",
)
cpu2 = Prosessor(
    "AMD", "Ryzen 7 7700X", 1500, 2800, "slitt", 8, 16, 4.5, 5.4, 32, "AM5", 105, "Nei"
)

gpu1 = Grafikkort(
    "Nvidia",
    "RTX 4080",
    6000,
    9000,
    "god",
    16,
    "GDDR6X",
    9728,
    2505,
    320,
    "3x DisplayPort 1.4, 1x HDMI 2.1",
)
gpu2 = Grafikkort(
    "AMD",
    "RX 7900 XTX",
    5000,
    8500,
    "god",
    24,
    "GDDR6",
    6144,
    2500,
    355,
    "2x DisplayPort 2.1, 1x HDMI 2.1",
)

ram1 = Ram(
    "Corsair",
    "Dominator Platinum",
    600,
    1200,
    "god",
    32,
    6000,
    "DDR5",
    30,
    2,
    1.1,
    "DIMM",
)
ram2 = Ram(
    "G.Skill", "Trident Z5", 500, 900, "god", 16, 5600, "DDR5", 28, 2, 1.1, "DIMM"
)

ssd1 = Lagring(
    "Samsung",
    "990 Pro",
    800,
    1500,
    "god",
    "2 TB",
    "NVMe",
    "PCIe 4.0",
    7450,
    6900,
    "M.2",
    0,
)
ssd2 = Lagring(
    "Seagate",
    "Barracuda",
    200,
    400,
    "slitt",
    "4 TB",
    "HDD",
    "SATA",
    190,
    190,
    '3.5"',
    256,
)

mobo1 = Hovedkort(
    "ASUS",
    "ROG Maximus Z790",
    2800,
    4500,
    "god",
    "LGA1700",
    "Z790",
    "ATX",
    4,
    128,
    3,
    "6x SATA, 4x M.2",
    "14x USB",
    "3.5.1",
)
mobo2 = Hovedkort(
    "MSI",
    "MAG B650 Tomahawk",
    1200,
    2200,
    "god",
    "AM5",
    "B650",
    "ATX",
    4,
    128,
    2,
    "4x SATA, 2x M.2",
    "10x USB",
    "1.B0",
)

psu1 = Psu(
    "Seasonic",
    "Focus GX-1000",
    1000,
    1800,
    "god",
    1000,
    "80+ Gold",
    "Full modulær",
    "24-pin, 2x CPU, 6x PCIe",
    "100-240V",
    135,
)
psu2 = Psu(
    "Corsair",
    "RM850x",
    800,
    1400,
    "slitt",
    850,
    "80+ Gold",
    "Full modulær",
    "24-pin, 2x CPU, 4x PCIe",
    "100-240V",
    135,
)

kjoel1 = Kjoeling(
    "Noctua", "NH-D15", 500, 900, "god", "Luft", 150, 1500, 24.6, 250, "Ingen"
)
kjoel2 = Kjoeling(
    "NZXT", "Kraken X73", 700, 1200, "god", "AIO", 120, 2800, 36, 300, "360mm"
)

kab1 = Kabinett(
    "Fractal",
    "Torrent",
    900,
    1500,
    "god",
    "ATX, mATX, ITX",
    "530x242x468",
    467,
    188,
    "6x 120mm / 3x 140mm",
    "420mm",
    "2x USB-A, 1x USB-C",
)
kab2 = Kabinett(
    "Lian Li",
    "O11 Dynamic EVO",
    1100,
    1800,
    "god",
    "ATX, mATX, ITX",
    "465x272x459",
    420,
    167,
    "10x 120mm",
    "360mm",
    "1x USB-A, 1x USB-C",
)

nett1 = Nettverkskort(
    "Intel", "AX210", 200, 400, "god", "PCIe", "2.4 Gbps", "WiFi 6E", "5.3"
)
nett2 = Nettverkskort(
    "TP-Link", "Archer TX3000E", 180, 350, "slitt", "PCIe", "2.4 Gbps", "WiFi 6", "5.0"
)

lyd1 = Lydkort("Creative", "Sound Blaster AE-9", 900, 1500, "god", "7.1", 384, "PCIe")
lyd2 = Lydkort("ASUS", "Xonar AE", 300, 600, "slitt", "7.1", 192, "PCIe")



vifte1 = Vifte(
    "Noctua", "NF-A12x25", 100, 200, "god", 120, 2000, 60.1, 22.6, "4-pin PWM"
)
vifte2 = Vifte(
    "be quiet!", "Silent Wings 4", 90, 180, "god", 120, 1600, 50.5, 18.9, "4-pin PWM"
)

# ============================================================
# LISTE + LØKKE
# ============================================================

alle_deler = [
    cpu1,
    cpu2,
    gpu1,
    gpu2,
    ram1,
    ram2,
    ssd1,
    ssd2,
    mobo1,
    mobo2,
    psu1,
    psu2,
    kjoel1,
    kjoel2,
    kab1,
    kab2,
    nett1,
    nett2,
    lyd1,
    lyd2,
    vifte1,
    vifte2,
]

for x in alle_deler:
    print("=" * 45)
    x.vis_komponent()
    print(f"  fortjeneste:        {x.fortjeneste()} kr")
