# efa-settings

[Interactive original](../upstream/app/public/viz/index.html?c=efa-settings) · [Poster](../upstream/app/public/viz/posters/efa-settings.webp)

The exact interactive implementation and data are retained locally. These rendered samples make figure-only knowledge searchable; they sample controls independently and do not enumerate every continuous value or combination. Interpret numerical examples using the figure’s stated evidence and limitations.

[Calculation and rendering source](../upstream/app/public/viz/assets/efa-settings-aR_rmTeq.js)

## Controls

```json
{}
```

Animation duration: 1 seconds. Samples include narrative transitions.

## Sample 1

Parameters: `{"t": 0}`

Does NCCL actually use the interconnect you configured?

our MoE with 16-way expert parallelism over two nodes: three runs in the order we tried them, the second and third each changing the row above

configuration

observed NCCL log

training throughput per GPU, TFLOP/s

The host’s EFA plugin, given by path

host /opt/amazon mounted, NCCL\_NET\_PLUGIN set to a path, FI\_PROVIDER\=efa

Could not find: libnccl-net-/opt/…/libnccl-net.so.so

Using network Socket

1.7

The plugin given by name

NCCL\_NET\_PLUGIN\=ofi, inherited LD\_LIBRARY\_PATH dropped

libefa.so.1: version \`EFA\_1.4’ not found

Using network Socket

1.7 to 1.8

The host’s RDMA libraries first

host libefa and libibverbs first in LD\_LIBRARY\_PATH

Selected provider is efa, fabric is efa-direct

Using network Libfabric

42.0

Three attempts to move our MoE’s cross-node all-to-all from sockets onto EFA, each row with its configuration, the NCCL log lines it produced and its throughput. Only the last reached EFA, and it trained over 20 times faster; a run on sockets still trains, so check NCCL’s debug log before timing anything across nodes.
