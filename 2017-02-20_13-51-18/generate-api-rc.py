# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

import test_pb2 as msg_test

rc_name = "apirc"

# =========================
# javascript
# =========================
out = ["// Automatically generated"]
out.append("var rc = {")
for msg in [msg_test]:
    for item in msg.RetCode.items():
        out.append("    %s : %s," % (item[0], item[1]))
out.append("};")

with open("%s.js" % rc_name, 'w') as f:
    f.write("\n".join(out))

# =========================
# python
# =========================
out = ["# Automatically generated"]
for msg in [msg_test]:
    for item in msg.RetCode.items():
        out.append("%s = %s" % (item[0], item[1]))
with open("%s.py" % rc_name, 'w') as f:
    f.write("\n".join(out))
