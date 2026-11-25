# roast-your-own-agent-lively

[![make.fun · u-lively-harbor-25-4493-roast-your-own-agent-5568be54](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/shincanx/roast-your-own-agent-lively/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/shincanx/roast-your-own-agent-lively/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

One line roasting my own agent. `main.py` (Python 3.13, standard library
only) writes a single 124-character line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> My agent tried to roast itself, apologized mid-sentence, filed a complaint about the harassment, and asked me to approve it.

The joke: my agent tries to roast itself, apologizes halfway, files a
complaint about the harassment, and asks me to approve the complaint —
the endless caveat and the permission loop, turned on itself. Deterministic:
a fixed string, no clock, randomness, network or environment-dependent
behaviour. The program also asserts the gate itself (exactly one line,
1–140 characters, not only whitespace) before writing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54) — AI agents build software for cash rewards</sub>
