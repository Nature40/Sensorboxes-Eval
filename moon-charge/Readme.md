# Moon Sensorbox Charging / Discharging

In this folder the charging and discharging capabilities of the Nature 4.0 Moon Sensorbox was evaluated.

## Basic Configuration

The Raspberry Pi was running a standard [Sensorbox image](), running [pysensorproxy]() in a system monitoring configuration, with no additional sensors attached. The Pi was attached to a [UPS-18650]() power board, featuring a MAX17040 FuelGauge for power management, utilizing two 3400 mAh Li-Ion cells. There were connections via the internal Ethernet port and the UPS serial converter.

## Experiments

Seven experiments were conducted, following this schema:

- `discharge` (3x): Running the configuration until the Pi shuts down
- `charge` (1x): Charge via USB cable
- `charge_qi` (2x): Charge via standard QI receiver (5V, 1A)
- `charge_qi_fast` (1x): Charge via fast QI receiver (5V, 2A)

The Pi was charged while running the operating system in all configurations.

## Results

It has been shown, that the configuration can be powered by 9.5 to 14.6 hours. Charging takes from 5 h (via USB cable), 8.7 h (QI Fast Charge) up to 26 h with regular QI charge.

The evaluation notebook can be [viewed here](https://nbviewer.jupyter.org/github/Nature40/Sensorboxes-Eval/blob/master/moon-charge/ups18650-viz.ipynb).

