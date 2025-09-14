# Open Memory

A deterministic, regex-driven memory layer for LLMs. It emphasizes precise retrieval from externally supplied textual corpora and integrates matched snippets back into the model’s context for grounded responses.

## TextMemory (Regex-based LLM memory layer)

<svg aria-roledescription="flowchart-v2" role="graphics-document document" viewBox="-8 -8 368.5703125 610.0625" style="max-width: 368.5703125px;" xmlns="http://www.w3.org/2000/svg" width="100%" id="mermaid-svg-1757887095677-x8gbcn4d1"><style>#mermaid-svg-1757887095677-x8gbcn4d1{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 .error-icon{fill:#bf616a;}#mermaid-svg-1757887095677-x8gbcn4d1 .error-text{fill:#bf616a;stroke:#bf616a;}#mermaid-svg-1757887095677-x8gbcn4d1 .edge-thickness-normal{stroke-width:2px;}#mermaid-svg-1757887095677-x8gbcn4d1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-svg-1757887095677-x8gbcn4d1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-svg-1757887095677-x8gbcn4d1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-svg-1757887095677-x8gbcn4d1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-svg-1757887095677-x8gbcn4d1 .marker{fill:rgba(204, 204, 204, 0.87);stroke:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 .marker.cross{stroke:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-svg-1757887095677-x8gbcn4d1 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 .cluster-label text{fill:#f3f3f3;}#mermaid-svg-1757887095677-x8gbcn4d1 .cluster-label span,#mermaid-svg-1757887095677-x8gbcn4d1 p{color:#f3f3f3;}#mermaid-svg-1757887095677-x8gbcn4d1 .label text,#mermaid-svg-1757887095677-x8gbcn4d1 span,#mermaid-svg-1757887095677-x8gbcn4d1 p{fill:rgba(204, 204, 204, 0.87);color:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 .node rect,#mermaid-svg-1757887095677-x8gbcn4d1 .node circle,#mermaid-svg-1757887095677-x8gbcn4d1 .node ellipse,#mermaid-svg-1757887095677-x8gbcn4d1 .node polygon,#mermaid-svg-1757887095677-x8gbcn4d1 .node path{fill:#191919;stroke:#242424;stroke-width:1px;}#mermaid-svg-1757887095677-x8gbcn4d1 .flowchart-label text{text-anchor:middle;}#mermaid-svg-1757887095677-x8gbcn4d1 .node .label{text-align:center;}#mermaid-svg-1757887095677-x8gbcn4d1 .node.clickable{cursor:pointer;}#mermaid-svg-1757887095677-x8gbcn4d1 .arrowheadPath{fill:#e6e6e6;}#mermaid-svg-1757887095677-x8gbcn4d1 .edgePath .path{stroke:rgba(204, 204, 204, 0.87);stroke-width:2.0px;}#mermaid-svg-1757887095677-x8gbcn4d1 .flowchart-link{stroke:rgba(204, 204, 204, 0.87);fill:none;}#mermaid-svg-1757887095677-x8gbcn4d1 .edgeLabel{background-color:#19191999;text-align:center;}#mermaid-svg-1757887095677-x8gbcn4d1 .edgeLabel rect{opacity:0.5;background-color:#19191999;fill:#19191999;}#mermaid-svg-1757887095677-x8gbcn4d1 .labelBkg{background-color:rgba(25, 25, 25, 0.5);}#mermaid-svg-1757887095677-x8gbcn4d1 .cluster rect{fill:rgba(64, 64, 64, 0.47);stroke:#30373a;stroke-width:1px;}#mermaid-svg-1757887095677-x8gbcn4d1 .cluster text{fill:#f3f3f3;}#mermaid-svg-1757887095677-x8gbcn4d1 .cluster span,#mermaid-svg-1757887095677-x8gbcn4d1 p{color:#f3f3f3;}#mermaid-svg-1757887095677-x8gbcn4d1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:#88c0d0;border:1px solid #30373a;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-svg-1757887095677-x8gbcn4d1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:rgba(204, 204, 204, 0.87);}#mermaid-svg-1757887095677-x8gbcn4d1 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}</style><g><marker orient="auto" markerHeight="12" markerWidth="12" markerUnits="userSpaceOnUse" refY="5" refX="6" viewBox="0 0 10 10" class="marker flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 0 L 10 5 L 0 10 z"/></marker><marker orient="auto" markerHeight="12" markerWidth="12" markerUnits="userSpaceOnUse" refY="5" refX="4.5" viewBox="0 0 10 10" class="marker flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointStart"><path style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 0 5 L 10 10 L 10 0 z"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="11" viewBox="0 0 10 10" class="marker flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-circleEnd"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5" refX="-1" viewBox="0 0 10 10" class="marker flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-circleStart"><circle style="stroke-width: 1; stroke-dasharray: 1, 0;" class="arrowMarkerPath" r="5" cy="5" cx="5"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="12" viewBox="0 0 11 11" class="marker cross flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-crossEnd"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><marker orient="auto" markerHeight="11" markerWidth="11" markerUnits="userSpaceOnUse" refY="5.2" refX="-1" viewBox="0 0 11 11" class="marker cross flowchart" id="mermaid-svg-1757887095677-x8gbcn4d1_flowchart-crossStart"><path style="stroke-width: 2; stroke-dasharray: 1, 0;" class="arrowMarkerPath" d="M 1,1 l 9,9 M 10,1 l -9,9"/></marker><g class="root"><g class="clusters"/><g class="edgePaths"><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-L LE-R" id="L-L-R-0" d="M106.291,33.5L106.291,37.667C106.291,41.833,106.291,50.167,106.291,57.617C106.291,65.067,106.291,71.633,106.291,74.917L106.291,78.2"/><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-R LE-M" id="L-R-M-0" d="M106.291,117L106.291,121.167C106.291,125.333,106.291,133.667,106.291,141.117C106.291,148.567,106.291,155.133,106.291,158.417L106.291,161.7"/><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-M LE-D" id="L-M-D-0" d="M106.291,200.5L106.291,204.667C106.291,208.833,106.291,217.167,106.357,224.7C106.423,232.234,106.555,238.967,106.621,242.334L106.687,245.701"/><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-D LE-F" id="L-D-F-0" d="M70.357,372.628L60.197,384.326C50.037,396.023,29.718,419.418,19.558,439.615C9.398,459.813,9.398,476.813,9.398,492.271C9.398,507.729,9.398,521.646,18.257,532.421C27.116,543.197,44.833,550.831,53.692,554.648L62.551,558.465"/><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-D LE-I" id="L-D-I-0" d="M143.225,372.628L153.218,384.326C163.211,396.023,183.198,419.418,193.191,435.94C203.184,452.463,203.184,462.113,203.184,466.938L203.184,471.763"/><path marker-end="url(#mermaid-svg-1757887095677-x8gbcn4d1_flowchart-pointEnd)" style="fill:none;" class="edge-thickness-normal edge-pattern-solid flowchart-link LS-I LE-F" id="L-I-F-0" d="M203.184,510.563L203.184,514.729C203.184,518.896,203.184,527.229,194.325,535.213C185.466,543.197,167.749,550.831,158.89,554.648L150.031,558.465"/></g><g class="edgeLabels"><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g><g transform="translate(9.3984375, 493.8125)" class="edgeLabel"><g transform="translate(-9.3984375, -9.25)" class="label"><foreignObject height="18.5" width="18.796875"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel">No</span></div></foreignObject></g></g><g transform="translate(203.18359375, 442.8125)" class="edgeLabel"><g transform="translate(-11.32421875, -9.25)" class="label"><foreignObject height="18.5" width="22.6484375"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel">Yes</span></div></foreignObject></g></g><g class="edgeLabel"><g transform="translate(0, 0)" class="label"><foreignObject height="0" width="0"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g transform="translate(106.291015625, 16.75)" id="flowchart-L-58" class="node default default flowchart-label"><rect height="33.5" width="42.5546875" y="-16.75" x="-21.27734375" ry="0" rx="0" style="" class="basic label-container"/><g transform="translate(-13.77734375, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="27.5546875"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">LLM</span></div></foreignObject></g></g><g transform="translate(106.291015625, 100.25)" id="flowchart-R-59" class="node default default flowchart-label"><rect height="33.5" width="176.96875" y="-16.75" x="-88.484375" ry="0" rx="0" style="" class="basic label-container"/><g transform="translate(-80.984375, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="161.96875"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">Regex + Flags + Search</span></div></foreignObject></g></g><g transform="translate(106.291015625, 183.75)" id="flowchart-M-60" class="node default default flowchart-label"><rect height="33.5" width="115.21875" y="-16.75" x="-57.609375" ry="0" rx="0" style="" class="basic label-container"/><g transform="translate(-50.109375, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="100.21875"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">Memory Layer</span></div></foreignObject></g></g><g transform="translate(106.291015625, 329.53125)" id="flowchart-D-61" class="node default default flowchart-label"><polygon style="" transform="translate(-79.03125,79.03125)" class="label-container" points="79.03125,0 158.0625,-79.03125 79.03125,-158.0625 0,-79.03125"/><g transform="translate(-54.78125, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="109.5625"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">Matches found?</span></div></foreignObject></g></g><g transform="translate(203.18359375, 493.8125)" id="flowchart-I-62" class="node default default flowchart-label"><rect height="33.5" width="298.7734375" y="-16.75" x="-149.38671875" ry="0" rx="0" style="" class="basic label-container"/><g transform="translate(-141.88671875, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="283.7734375"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">Inject extracted memory into messages</span></div></foreignObject></g></g><g transform="translate(106.291015625, 577.3125)" id="flowchart-F-63" class="node default default flowchart-label"><rect height="33.5" width="152.3359375" y="-16.75" x="-76.16796875" ry="0" rx="0" style="" class="basic label-container"/><g transform="translate(-68.66796875, -9.25)" style="" class="label"><rect/><foreignObject height="18.5" width="137.3359375"><div style="display: inline-block; white-space: nowrap;" xmlns="http://www.w3.org/1999/xhtml"><span class="nodeLabel">LLM Final Response</span></div></foreignObject></g></g></g></g></g></svg>

### How it works

1. The LLM proposes a regex pattern plus flags (the "search plan").
2. We execute that search against a simple memory layer (a text/Markdown file).
3. We extract only the matching snippets and inject them into the LLM messages.
4. The LLM produces the final response with just the relevant memory.

### Why this approach

- We hypothesize that high-quality regex/word search over plain text can be competitive on many tasks by precisely matching terms, formats, and structures without embedding drift.
- It keeps the system simple, fast, and transparent: no indexes, no vector stores, just a file and robust search.
- It limits context to only the matches, reducing prompt bloat while preserving fidelity.

### Programmatic usage

```python
import re
from open_memory import TextMemory

mem = TextMemory("Hello world. Error: disk full.\n\n## Header\nNext line.")
matches = mem.search_matches(r"error", flags=re.IGNORECASE)
for m in matches:
    print(m.text, m.span)
```

## Design goals

- **Simplicity**: a single text/markdown file is the memory.
- **Power**: the agent issues precise regex queries to find information.
- **Portability**: no server required; CLI and a tiny Python API.

## Quick Start

### Prerequisites

- Python 3.12+
- uv (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Mellow-Artificial-Intelligence/open-memory
cd open-memory
```

2. Install dependencies:
```bash
uv sync
```

3. Run a quick snippet:
```bash
uv run python -c "import re; from open_memory import TextMemory; m=TextMemory('An error occurred'); print([x.text for x in m.search_matches('error', flags=re.IGNORECASE)])"
```
## Notes on data

Open Memory operates over user-provided textual corpora (e.g., logs, notes, documentation). Typical usage reads file contents into `TextMemory` and applies deterministic regex-based retrieval to integrate matched snippets into downstream prompts.



## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
