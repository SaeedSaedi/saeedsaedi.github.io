"""Build the case studies for saeedsaedi.github.io.

One content source (CASES below) produces:
  • work/<slug>.html — one page per case study
  • the card grid in index.html, between <!-- WORK:START --> and <!-- WORK:END -->

    python3 _tools/build-work.py

Edit case-study text and diagrams here, never in the generated HTML.
(_tools/ starts with "_", so GitHub Pages' Jekyll build does not publish it.)

Content rules: facts come from RESUME.md / linkedin/ / ai-skills/; nothing
about internal service names, architecture beyond the public stack, security,
custody, incidents, vendors, compliance or people; no numbers that are not
already public on the site or résumé. Diagrams are illustrative.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ─── Diagrams (inline SVG so they use the page fonts) ────────────────────────

SVG_OWNERSHIP = """<svg viewBox="0 0 560 340" role="img" aria-label="Before: one sprint plan tangled across services. After: three squads that own their services, with explicit dependencies.">
  <defs><marker id="arw-own" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#818cf8"/></marker></defs>
  <text x="8" y="20" class="dg-label">BEFORE</text>
  <text x="8" y="40" class="dg-sub">One sprint plan, 31 services</text>
  <g stroke="#34343c" stroke-width="1">
    <line x1="130" y1="94" x2="130" y2="190"/><line x1="186.4" y1="112.3" x2="130" y2="190"/>
    <line x1="221.3" y1="160.3" x2="130" y2="190"/><line x1="221.3" y1="219.7" x2="130" y2="190"/>
    <line x1="186.4" y1="267.7" x2="130" y2="190"/><line x1="130" y1="286" x2="130" y2="190"/>
    <line x1="73.6" y1="267.7" x2="130" y2="190"/><line x1="38.7" y1="219.7" x2="130" y2="190"/>
    <line x1="38.7" y1="160.3" x2="130" y2="190"/><line x1="73.6" y1="112.3" x2="130" y2="190"/>
  </g>
  <g stroke="#55555f" stroke-width="1" stroke-dasharray="3 4">
    <line x1="186.4" y1="112.3" x2="73.6" y2="267.7"/><line x1="221.3" y1="160.3" x2="38.7" y2="219.7"/>
    <line x1="130" y1="94" x2="186.4" y2="267.7"/><line x1="73.6" y1="112.3" x2="221.3" y2="219.7"/>
  </g>
  <g fill="#17171b" stroke="#46464f">
    <rect x="122" y="86" width="16" height="16" rx="3"/><rect x="178.4" y="104.3" width="16" height="16" rx="3"/>
    <rect x="213.3" y="152.3" width="16" height="16" rx="3"/><rect x="213.3" y="211.7" width="16" height="16" rx="3"/>
    <rect x="178.4" y="259.7" width="16" height="16" rx="3"/><rect x="122" y="278" width="16" height="16" rx="3"/>
    <rect x="65.6" y="259.7" width="16" height="16" rx="3"/><rect x="30.7" y="211.7" width="16" height="16" rx="3"/>
    <rect x="30.7" y="152.3" width="16" height="16" rx="3"/><rect x="65.6" y="104.3" width="16" height="16" rx="3"/>
  </g>
  <rect x="94" y="174" width="72" height="32" rx="8" fill="#16163a" stroke="#6366f1"/>
  <text x="130" y="194" text-anchor="middle" class="dg-small" style="fill:#a5b4fc">SPRINT</text>
  <g fill="#fbbf24"><circle cx="158.2" cy="151.2" r="4"/><circle cx="84.4" cy="204.9" r="4"/><circle cx="117.9" cy="144.5" r="4"/></g>
  <circle cx="12" cy="325" r="4" fill="#fbbf24"/><text x="22" y="329" class="dg-sub">blocked dependency</text>
  <line x1="280" y1="12" x2="280" y2="328" stroke="#26262c" stroke-dasharray="3 5"/>
  <text x="304" y="20" class="dg-label">AFTER</text>
  <text x="304" y="40" class="dg-sub">3 squads, clear owners</text>
  <g fill="rgba(255,255,255,0.015)" stroke="#3a3a42" stroke-dasharray="4 4">
    <rect x="304" y="78" width="104" height="104" rx="14"/><rect x="448" y="78" width="104" height="104" rx="14"/><rect x="376" y="214" width="104" height="104" rx="14"/>
  </g>
  <g fill="rgba(34,211,238,0.16)"><circle cx="320" cy="96" r="9"/><circle cx="464" cy="96" r="9"/><circle cx="392" cy="232" r="9"/></g>
  <g fill="#22d3ee"><circle cx="320" cy="96" r="4.5"/><circle cx="464" cy="96" r="4.5"/><circle cx="392" cy="232" r="4.5"/></g>
  <text x="332" y="100" class="dg-small">BACKEND</text><text x="476" y="100" class="dg-small">INFRA</text><text x="404" y="236" class="dg-small">BLOCKCHAIN</text>
  <g fill="#17171b" stroke="#55555f">
    <rect x="334" y="120" width="16" height="16" rx="3"/><rect x="362" y="120" width="16" height="16" rx="3"/><rect x="334" y="148" width="16" height="16" rx="3"/><rect x="362" y="148" width="16" height="16" rx="3"/>
    <rect x="478" y="120" width="16" height="16" rx="3"/><rect x="506" y="120" width="16" height="16" rx="3"/><rect x="478" y="148" width="16" height="16" rx="3"/><rect x="506" y="148" width="16" height="16" rx="3"/>
    <rect x="406" y="256" width="16" height="16" rx="3"/><rect x="434" y="256" width="16" height="16" rx="3"/><rect x="406" y="284" width="16" height="16" rx="3"/><rect x="434" y="284" width="16" height="16" rx="3"/>
  </g>
  <g stroke="#818cf8" stroke-width="1.5" fill="none" marker-end="url(#arw-own)">
    <line x1="410" y1="130" x2="444" y2="130"/><path d="M356 184 V250 Q356 266 372 266"/><path d="M500 184 V250 Q500 266 484 266"/>
  </g>
  <line x1="304" y1="325" x2="322" y2="325" stroke="#818cf8" stroke-width="1.5"/><text x="328" y="329" class="dg-sub">explicit dependency</text>
  <circle cx="462" cy="325" r="4" fill="#22d3ee"/><text x="472" y="329" class="dg-sub">owner</text>
</svg>"""


def _board_tiles():
    shipped, risk = {0, 3, 9, 16, 19, 24, 30}, {5, 13, 22, 27}
    out = []
    for i in range(31):
        c, r = i % 8, i // 8
        x, y = 20 + c * 61, 52 + r * 38
        tone = "129,140,248" if i in shipped else "251,191,36" if i in risk else "52,211,153"
        out.append(f'<rect x="{x}" y="{y}" width="53" height="30" rx="6" fill="rgba({tone},.10)" stroke="rgba({tone},.5)"/>'
                   f'<rect x="{x + 8}" y="{y + 20}" width="{14 + (i * 37) % 24}" height="3" rx="1.5" fill="rgba({tone},.8)"/>')
    return "\n    ".join(out)


SVG_BOARD = f"""<svg viewBox="0 0 520 300" role="img" aria-label="Illustrative delivery board: 31 services marked on track, at risk or shipped, with velocity, risk and release-confidence bars.">
  <rect x="0.5" y="0.5" width="519" height="299" rx="12" fill="#0d0d10" stroke="#26262b"/>
  <g fill="#2c2c33"><circle cx="18" cy="18" r="4"/><circle cx="32" cy="18" r="4"/><circle cx="46" cy="18" r="4"/></g>
  <text x="64" y="22" class="dg-small">delivery · 31 services</text>
  <circle cx="466" cy="18" r="3.5" fill="#34d399"/><text x="476" y="22" class="dg-small" style="fill:#34d399">LIVE</text>
  <line x1="0.5" y1="36" x2="519.5" y2="36" stroke="#1e1e23"/>
  <g>
    {_board_tiles()}
  </g>
  <text x="20" y="226" class="dg-small">VELOCITY</text>
  <text x="187" y="226" class="dg-small">RISK</text>
  <text x="354" y="226" class="dg-small">RELEASE CONFIDENCE</text>
  <g fill="#1e1e23"><rect x="20" y="236" width="146" height="6" rx="3"/><rect x="187" y="236" width="146" height="6" rx="3"/><rect x="354" y="236" width="146" height="6" rx="3"/></g>
  <rect x="20" y="236" width="104" height="6" rx="3" fill="#818cf8"/>
  <rect x="187" y="236" width="44" height="6" rx="3" fill="#fbbf24"/>
  <rect x="354" y="236" width="118" height="6" rx="3" fill="#22d3ee"/>
  <rect x="20" y="268" width="10" height="10" rx="2" fill="rgba(52,211,153,.12)" stroke="rgba(52,211,153,.6)"/><text x="36" y="277" class="dg-sub">on track</text>
  <rect x="104" y="268" width="10" height="10" rx="2" fill="rgba(251,191,36,.12)" stroke="rgba(251,191,36,.65)"/><text x="120" y="277" class="dg-sub">at risk</text>
  <rect x="180" y="268" width="10" height="10" rx="2" fill="rgba(129,140,248,.16)" stroke="rgba(129,140,248,.6)"/><text x="196" y="277" class="dg-sub">shipped</text>
  <text x="500" y="277" text-anchor="end" class="dg-sub" font-style="italic">illustrative</text>
</svg>"""


def _chip(x, w, label):
    return (f'<rect x="{x}" y="248" width="{w}" height="24" rx="7" fill="#121215" stroke="#2b2b31"/>'
            f'<path d="M{x + 10} 260 l3 3 l6 -6" fill="none" stroke="#34d399" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<text x="{x + 24}" y="264" class="dg-small" style="fill:#a1a1aa">{label}</text>')


SVG_RELEASE = f"""<svg viewBox="0 0 520 300" role="img" aria-label="Illustrative staged rollout: internal accounts first, then a small share of users, a larger share and everyone, with a tested kill switch and a rollback threshold set before launch.">
  <rect x="0.5" y="0.5" width="519" height="299" rx="12" fill="#0d0d10" stroke="#26262b"/>
  <g fill="#2c2c33"><circle cx="18" cy="18" r="4"/><circle cx="32" cy="18" r="4"/><circle cx="46" cy="18" r="4"/></g>
  <text x="64" y="22" class="dg-small">release plan · touches money</text>
  <text x="424" y="22" text-anchor="end" class="dg-small">kill switch</text>
  <rect x="432" y="10" width="30" height="16" rx="8" fill="rgba(52,211,153,.16)" stroke="rgba(52,211,153,.6)"/>
  <circle cx="453" cy="18" r="5" fill="#34d399"/>
  <text x="470" y="22" class="dg-small" style="fill:#34d399">TESTED</text>
  <line x1="0.5" y1="36" x2="519.5" y2="36" stroke="#1e1e23"/>
  <text x="20" y="60" class="dg-small">1 INTERNAL</text><text x="144" y="60" class="dg-small">2 SMALL SHARE</text>
  <text x="268" y="60" class="dg-small">3 LARGER SHARE</text><text x="392" y="60" class="dg-small">4 EVERYONE</text>
  <g fill="#1e1e23"><rect x="20" y="70" width="108" height="8" rx="4"/><rect x="144" y="70" width="108" height="8" rx="4"/><rect x="268" y="70" width="108" height="8" rx="4"/><rect x="392" y="70" width="108" height="8" rx="4"/></g>
  <rect x="20" y="70" width="8" height="8" rx="4" fill="#818cf8"/><rect x="144" y="70" width="20" height="8" rx="4" fill="#818cf8"/>
  <rect x="268" y="70" width="50" height="8" rx="4" fill="#818cf8"/><rect x="392" y="70" width="108" height="8" rx="4" fill="#22d3ee"/>
  <text x="20" y="110" class="dg-small">ERROR RATE</text>
  <text x="500" y="122" text-anchor="end" class="dg-small" style="fill:#fbbf24">ROLLBACK IF CROSSED</text>
  <line x1="20" y1="130" x2="500" y2="130" stroke="#fbbf24" stroke-dasharray="5 5" opacity=".75"/>
  <g stroke="#26262c" stroke-dasharray="2 4"><line x1="136" y1="96" x2="136" y2="226"/><line x1="260" y1="96" x2="260" y2="226"/><line x1="384" y1="96" x2="384" y2="226"/></g>
  <line x1="20" y1="226" x2="500" y2="226" stroke="#2b2b31"/>
  <polyline points="20,206 60,203 100,208 136,200 172,205 212,198 260,203 300,197 340,204 384,199 424,203 462,196 500,200" fill="none" stroke="#22d3ee" stroke-width="1.6" stroke-linejoin="round"/>
  {_chip(20, 62, "logs")}{_chip(90, 82, "metrics")}{_chip(180, 75, "alerts")}{_chip(263, 82, "runbook")}
  <text x="500" y="266" text-anchor="end" class="dg-sub" font-style="italic">illustrative</text>
</svg>"""

SVG_OUTPUT = """<svg viewBox="0 0 520 300" role="img" aria-label="Monthly output grew from 3,000 to 25,000 units, an eightfold increase.">
  <defs>
    <linearGradient id="barGrad" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#4f46e5"/><stop offset=".55" stop-color="#6366f1"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
    <linearGradient id="txtGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#c7d2fe"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
    <marker id="arw-out" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#67e8f9"/></marker>
  </defs>
  <rect x="0.5" y="0.5" width="519" height="299" rx="12" fill="#0d0d10" stroke="#26262b"/>
  <line x1="32" y1="236" x2="488" y2="236" stroke="#2b2b31"/>
  <rect x="112" y="213" width="92" height="23" rx="5" fill="#26262c" stroke="#3a3a42"/>
  <rect x="316" y="46" width="92" height="190" rx="6" fill="url(#barGrad)" opacity=".92"/>
  <text x="158" y="200" text-anchor="middle" class="dg-num">3K</text>
  <text x="362" y="34" text-anchor="middle" class="dg-num">25K</text>
  <path d="M210 206 C262 206 270 100 306 92" fill="none" stroke="#67e8f9" stroke-width="1.5" stroke-dasharray="4 5" marker-end="url(#arw-out)"/>
  <text x="228" y="132" text-anchor="middle" class="dg-big" fill="url(#txtGrad)">8×</text>
  <text x="158" y="260" text-anchor="middle" class="dg-small">BEFORE</text>
  <text x="362" y="260" text-anchor="middle" class="dg-small">AFTER</text>
  <text x="260" y="284" text-anchor="middle" class="dg-sub">units per month</text>
</svg>"""


def _rows(x, y, widths, colors):
    out = []
    for k, (w, col) in enumerate(zip(widths, colors)):
        yy = y + k * 12
        out.append(f'<rect x="{x}" y="{yy}" width="6" height="6" rx="1.5" fill="{col}"/>'
                   f'<line x1="{x + 14}" y1="{yy + 3}" x2="{x + 14 + w}" y2="{yy + 3}" stroke="#3a3a42" stroke-width="3" stroke-linecap="round"/>')
    return "".join(out)


SVG_FACTORY = f"""<svg viewBox="0 0 520 300" role="img" aria-label="Illustrative: manual tracking replaced by two internal systems, for packaging and maintenance, that feed KPI reports and are used by 21 people.">
  <defs>
    <marker id="arw-fac" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#818cf8"/></marker>
    <linearGradient id="facGrad" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#4f46e5"/><stop offset="1" stop-color="#22d3ee"/></linearGradient>
  </defs>
  <rect x="0.5" y="0.5" width="519" height="299" rx="12" fill="#0d0d10" stroke="#26262b"/>
  <text x="24" y="34" class="dg-label">BEFORE</text>
  <text x="24" y="52" class="dg-sub">manual tracking</text>
  <rect x="44" y="92" width="92" height="120" rx="6" fill="#121215" stroke="#2b2b31"/>
  <rect x="36" y="84" width="92" height="120" rx="6" fill="#141418" stroke="#34343c"/>
  <rect x="28" y="76" width="92" height="120" rx="6" fill="#17171b" stroke="#3a3a42"/>
  <g stroke="#3a3a42" stroke-width="3" stroke-linecap="round">
    <line x1="40" y1="98" x2="104" y2="98"/><line x1="40" y1="114" x2="92" y2="114"/><line x1="40" y1="130" x2="98" y2="130"/>
    <line x1="40" y1="146" x2="84" y2="146"/><line x1="40" y1="162" x2="96" y2="162"/><line x1="40" y1="178" x2="76" y2="178"/>
  </g>
  <g fill="#fbbf24"><circle cx="108" cy="130" r="3.5"/><circle cx="88" cy="178" r="3.5"/></g>
  <line x1="146" y1="150" x2="190" y2="150" stroke="#818cf8" stroke-width="1.5" marker-end="url(#arw-fac)"/>
  <text x="206" y="34" class="dg-label">AFTER</text>
  <text x="206" y="52" class="dg-sub">two internal systems</text>
  <rect x="206" y="72" width="156" height="72" rx="8" fill="#121215" stroke="#2b2b31"/>
  <text x="218" y="90" class="dg-small">PACKAGING</text>
  {_rows(218, 100, (88, 70, 96), ("#22d3ee", "#818cf8", "#22d3ee"))}
  <rect x="206" y="156" width="156" height="72" rx="8" fill="#121215" stroke="#2b2b31"/>
  <text x="218" y="174" class="dg-small">MAINTENANCE</text>
  {_rows(218, 184, (76, 98, 64), ("#818cf8", "#22d3ee", "#818cf8"))}
  <line x1="372" y1="150" x2="404" y2="150" stroke="#818cf8" stroke-width="1.5" marker-end="url(#arw-fac)"/>
  <rect x="414" y="80" width="86" height="140" rx="10" fill="#121215" stroke="#2b2b31"/>
  <text x="426" y="100" class="dg-small">KPI</text>
  <line x1="424" y1="204" x2="490" y2="204" stroke="#2b2b31"/>
  <g fill="url(#facGrad)"><rect x="428" y="170" width="10" height="34" rx="2"/><rect x="444" y="152" width="10" height="52" rx="2"/><rect x="460" y="160" width="10" height="44" rx="2"/><rect x="476" y="138" width="10" height="66" rx="2"/></g>
  <rect x="206" y="246" width="84" height="26" rx="8" fill="#121215" stroke="#2b2b31"/><text x="218" y="263" class="dg-small" style="fill:#a1a1aa">21 users</text>
  <rect x="298" y="246" width="92" height="26" rx="8" fill="#121215" stroke="#2b2b31"/><text x="310" y="263" class="dg-small" style="fill:#a1a1aa">2 systems</text>
  <text x="500" y="266" text-anchor="end" class="dg-sub" font-style="italic">illustrative</text>
</svg>"""

# ─── Content ──────────────────────────────────────────────────────────────────
# results: (value, label, is_word) — is_word renders a smaller value for words.

CASES = [
    dict(
        slug="service-ownership", org="Kifpool.me", area="Delivery",
        title="From one sprint plan to service ownership",
        card_text="Delivery for 31 microservices ran on one shared sprint plan, so cross-team dependencies kept surfacing mid-sprint. I moved delivery to service-level ownership and put dependencies on the table before each sprint.",
        card_num="−30%", card_label="cross-team dependency blockers, and more predictable releases",
        lead="Thirty-one microservices shared one sprint plan, and cross-team dependencies kept surfacing halfway through the sprint. I moved delivery to service-level ownership and mapped dependencies before each sprint started. Cross-team blockers fell by 30%, and releases became more predictable.",
        glance=[("Role", "Technical Product Manager"), ("Team", "20 engineers, 3 squads"), ("Scope", "31 microservices"), ("Result", "−30% cross-team blockers")],
        svg=SVG_OWNERSHIP,
        caption="Before: one plan across every service, with dependencies found mid-sprint. After: three squads that own their services, with dependencies agreed up front. Illustrative.",
        situation="<p>Kifpool.me is a cryptocurrency exchange with more than two million users. Behind it are 31 microservices, from the exchange engine and order management to pricing and blockchain integrations. Twenty engineers build them in three squads: backend, infrastructure and blockchain. We work in two-week sprints.</p>",
        problem="<p>Planning happened as one sprint for everyone. Each engineer planned their own piece, but nobody owned the picture across services. When a feature touched two or three services, the dependency usually showed up halfway through the sprint: one service changed a contract that another was already building against. Both slipped, and the sprint goal slipped with them.</p><p>In a system this size, that pattern was the biggest single reason sprint goals were missed.</p>",
        did=[
            ("Every service has an owner.", "Each squad owns its services end to end, from planning to release, so someone is always accountable for a change and its effects."),
            ("Dependencies are mapped before the sprint, not during it.", "Any feature that touches more than one service gets a dependency map at planning, and shared API contracts are agreed before parallel work starts."),
            ("Slips show up early.", "A short check on day six of each sprint, plus a “cut first if tight” list, means we adjust while there is still time."),
            ("Commitments match capacity.", "Velocity from past sprints sets how much we take on, so plans are realistic from the start."),
        ],
        quote="Dependency management means catching the collision on day zero, not day eight.",
        results=[("−30%", "cross-team dependency blockers", False), ("95%+", "on-time delivery across 31 services", False), ("Earlier", "conflicts now surface at planning instead of mid-sprint", True)],
        learned="<p>Most delivery delays are coordination problems that look like engineering problems. Making ownership and dependencies explicit did more for our speed than any push to work faster.</p>",
    ),
    dict(
        slug="delivery-visibility", org="Kifpool.me", area="Visibility",
        title="Real-time delivery visibility for the C-suite",
        card_text="An org-wide tracking framework that shows velocity, risk and release confidence for every service, so leadership sees delivery as it happens instead of in status meetings.",
        card_num="31/31", card_label="services tracked in real time",
        lead="Leadership needed to know where delivery stood without waiting for the next status meeting. I built an org-wide tracking framework that shows velocity, risk and release confidence for all 31 services in real time, backed by a short weekly update and a scored risk register.",
        glance=[("Role", "Technical Product Manager"), ("Audience", "CEO, CTO and the squads"), ("Scope", "31 microservices"), ("Result", "Live view of delivery")],
        svg=SVG_BOARD,
        caption="One view of every service: on track, at risk or shipped, with velocity, risk and release confidence. Illustrative data.",
        situation="<p>With 31 services moving in parallel across three squads, the CEO and CTO needed clear answers to simple questions. What ships this sprint? What is at risk? How confident are we in the next release?</p>",
        problem="<p>Status lived in many places and was often out of date by the time it reached leadership. Getting an answer took a meeting, and risks tended to surface late, when the options for fixing them were fewer and more expensive.</p>",
        did=[
            ("Three signals for every service:", "velocity, risk and release confidence, tracked the same way across all 31 services."),
            ("A risk register for the quarter.", "Each risk is scored for likelihood and impact on a 1–5 scale, and has an owner and a trigger for escalation."),
            ("A short weekly update for leadership:", "delivery status, one escalation and one metric that matters."),
            ("One version of the truth.", "The same numbers feed sprint retrospectives, so the team and leadership look at the same picture."),
        ],
        quote="Too much detail buries the signal. Too little creates anxiety.",
        results=[("31/31", "services tracked in real time", False), ("Weekly", "update: status, one escalation, one metric", True), ("Earlier", "risks are escalated before they turn into misses", True)],
        learned="<p>Visibility changes the conversation. When leadership can see what the team sees, meetings are for decisions, not for updates.</p>",
    ),
    dict(
        slug="safe-releases", org="Kifpool.me", area="Reliability",
        title="Releases that protect people’s money",
        card_text="On an exchange, a bad release can touch people’s money. I made rollout plans, rollback paths and monitoring a standard part of shipping anything that touches financial data.",
        card_num="48 h", card_label="from a serious incident to a blameless postmortem, with fixes tracked to done",
        lead="Crypto markets move fast, and the busiest moments are exactly when an exchange can least afford a broken release. I made release plans, staged rollouts, rollback paths and monitoring a standard part of shipping anything that touches financial data.",
        glance=[("Role", "Technical Product Manager"), ("Applies to", "Changes that touch financial data"), ("Practice", "Flags, staged rollouts, runbooks"), ("Standard", "Rollback path before launch")],
        svg=SVG_RELEASE,
        caption="A staged rollout with a tested kill switch and a rollback threshold agreed before launch. Illustrative.",
        situation="<p>Kifpool.me handles thousands of transactions a day across trading, custody and settlement, and crypto prices can move sharply within minutes. Users expect the app to work best exactly when the market is busiest.</p>",
        problem="<p>Speed and safety pull in opposite directions. The team ships every two weeks, and some of those changes touch balances, orders or prices. A release that goes wrong at the wrong moment costs users money and trust, and trust is hard to win back.</p>",
        did=[
            ("A release plan for anything that touches financial data:", "what changes, how it rolls out, what success looks like, and the exact conditions for rolling back."),
            ("Feature flags and staged rollouts.", "New behaviour reaches internal accounts first, then a growing share of users, then everyone. The kill switch is tested before launch, not during an incident."),
            ("Nothing ships blind.", "Before a new service reaches production it needs structured logs, at least four key metrics, two alert rules and a basic runbook."),
            ("A second look where it matters.", "Changes to financial logic or concurrent operations get a focused review, instead of treating every pull request the same."),
            ("Blameless postmortems within 48 hours", "of a serious incident, with action items that feed straight into the risk register."),
        ],
        quote="Facts first, cause second, prevention third.",
        results=[("Staged", "rollouts for changes that touch money", True), ("4 + 2", "key metrics and alert rules before a new service ships", False), ("48 h", "to a blameless postmortem after a serious incident", False)],
        learned="<p>Reliability is a product feature. Users never see the release plan, but they feel it on the days the market is busiest.</p>",
    ),
    dict(
        slug="production-line", org="Toosalem Industrial", area="Operations",
        title="Scaling a production line 8×",
        card_text="Designed a new production line and restructured shift operations to take output from 3,000 to 25,000 units a month, with less waste and less downtime.",
        card_num="8×", card_label="monthly output, with −26% waste and −18% downtime",
        lead="I took monthly output from 3,000 to 25,000 units by designing a new production line and changing how three shifts worked together. Efficiency rose 40%, material waste fell 26% and unplanned downtime fell 18%.",
        glance=[("Role", "Production Manager"), ("Team", "~80 people, 3 shifts"), ("Worked with", "Engineering, foundry, HR, supply chain"), ("Result", "3,000 → 25,000 units a month")],
        svg=SVG_OUTPUT,
        caption="Monthly output before and after the new line. Illustrative scale.",
        situation="<p>Toosalem is an automotive manufacturer. I ran production: about 80 people across three shifts, working closely with engineering, the foundry, HR and the supply chain.</p>",
        problem="<p>The existing line and shift structure could not produce anywhere near the volume the business needed. Pushing the existing setup harder would only have added waste and downtime.</p>",
        did=[
            ("Designed a new production line", "and rebuilt the flow of work around it."),
            ("Restructured the three shifts", "and reengineered the processes between them."),
            ("One plan across departments.", "Engineering, the foundry, HR and the supply chain worked from the same plan and the same numbers."),
            ("Root causes, not symptoms.", "Data on waste and downtime pointed to root causes, and a preventive maintenance program dealt with them before they stopped the line."),
            ("Software where manual tracking failed.", "Two internal systems replaced manual tracking for packaging and maintenance, described in the next case study."),
        ],
        quote="A small knot in a process becomes a serious blocker at scale.",
        results=[("8×", "monthly output, 3,000 → 25,000 units", False), ("+40%", "efficiency across three shifts", False), ("−26%", "material waste", False), ("−18%", "unplanned downtime", False)],
        learned="<p>Throughput, quality and waste are measurable in software too. I still plan sprints the way I learned to plan a production line: find the bottleneck first.</p>",
    ),
    dict(
        slug="factory-software", org="Toosalem Industrial", area="Internal product",
        title="Software for a factory floor",
        card_text="Production depended on manual tracking. I built two internal systems, for packaging and for maintenance, that 21 people used and that made our KPI reporting more accurate.",
        card_num="21", card_label="people using two internal systems",
        lead="Packaging and maintenance were tracked by hand, and the numbers that reached management were hard to trust. I built and deployed two internal systems that replaced manual tracking for 21 people and made KPI reporting more accurate.",
        glance=[("Role", "Production Manager, and builder of the tools"), ("Users", "21 people"), ("Systems", "Packaging and maintenance management"), ("Result", "Manual tracking replaced")],
        svg=SVG_FACTORY,
        caption="From manual tracking to two internal systems that feed KPI reports. Illustrative.",
        situation="<p>On the factory floor, packaging and maintenance were tracked manually. The KPIs built on that data were only as good as the records behind them.</p>",
        problem="<p>Management made decisions on numbers that were late or incomplete. Maintenance was mostly reactive, because there was no reliable history of what had been done and when.</p>",
        did=[
            ("Started from the daily routine", "of the people who would use the tools: operators, supervisors and maintenance staff."),
            ("Built two focused systems:", "packaging management and maintenance management."),
            ("Deployed and supported them in production", "for 21 users, and retired manual tracking."),
            ("Connected the data", "to KPI reporting and to the preventive maintenance program."),
        ],
        quote="Find where the work is painful, build the smallest thing that fixes it, and make sure people actually use it.",
        results=[("2", "internal systems in production", False), ("21", "people using them", False), ("Accurate", "KPI reporting instead of manual tallies", True)],
        learned="<p>This was product work before I had the title: start from the people who do the job, solve the painful part first, and check that the tool is actually used.</p>",
    ),
]

# ─── Templates ────────────────────────────────────────────────────────────────

SITE = "https://saeedsaedi.github.io"


def rich(text):
    """HTML-only typography fixes for titles (not used in <title> or meta tags)."""
    return text.replace("C-suite", '<span class="nowrap">C-suite</span>')


def head(c):
    title = html.escape(f"{c['title']} — Saeed Saedi")
    desc = html.escape(c["card_text"], quote=True)
    url = f"{SITE}/work/{c['slug']}.html"
    return f"""<!DOCTYPE html>
<html lang="en" class="serif">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{url}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{SITE}/assets/og-image.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:url" content="{url}" />
  <meta property="og:type" content="article" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" href="../favicon.ico" sizes="16x16 32x32 48x48" />
  <link rel="apple-touch-icon" href="../apple-touch-icon.png" />
  <script>document.documentElement.classList.add('js');</script>
  <link rel="preload" href="../assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="preload" href="../assets/fonts/instrument-serif-regular.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="../style.css" />
</head>"""


NAV = """<header class="nav">
  <div class="wrap nav__inner">
    <a class="brand" href="../"><span class="brand__mark" aria-hidden="true">SS</span>Saeed Saedi</a>
    <nav class="nav__links" id="nav-links" aria-label="Primary">
      <a href="../#work">Work</a>
      <a href="../#path">Path</a>
      <a href="../#experience">Experience</a>
      <a href="../resume.html" target="_blank" rel="noopener">Résumé ↗</a>
    </nav>
    <a class="btn btn--ghost btn--sm" href="../#contact">Get in touch</a>
    <button class="nav__menu" type="button" aria-expanded="false" aria-controls="nav-links">Menu</button>
  </div>
</header>"""

FOOT = """<footer class="footer">
  <div class="wrap">
    <span>© <span id="year">2026</span> Saeed Saedi</span>
    <span>Hand-built — HTML and CSS, no frameworks · <a href="https://github.com/SaeedSaedi/saeedsaedi.github.io" target="_blank" rel="noopener">Source ↗</a></span>
  </div>
</footer>

<script src="../script.js" defer></script>
</body>
</html>
"""


def card(c, featured):
    cls = "case case--featured" if featured else "case"
    return f"""      <a class="{cls}" href="work/{c['slug']}.html">
        <div class="case__visual">
          {c['svg']}
        </div>
        <div class="case__body">
          <p class="case__meta">{c['org']} · {c['area']}</p>
          <h3 class="case__title">{rich(c['title'])}</h3>
          <p class="case__text">{c['card_text']}</p>
          <div class="case__result"><span class="case__num">{c['card_num']}</span><span class="case__num-label">{c['card_label']}</span></div>
          <span class="case__cta">Read the case study</span>
        </div>
      </a>
"""


def page(c, nxt):
    glance = "\n        ".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in c["glance"])
    did = "\n          ".join(f"<li><strong>{a}</strong> {b}</li>" for a, b in c["did"])
    results = "\n          ".join(
        f'<div><b{" class=\"word\"" if w else ""}>{v}</b><span>{lbl}</span></div>' for v, lbl, w in c["results"])
    return f"""{head(c)}
<body>

{NAV}

<main class="cs">
  <article>
    <div class="wrap">
      <a class="cs__back" href="../#work">← All work</a>
      <p class="eyebrow">Case study · {c['org']} · {c['area']}</p>
      <h1 class="cs__title">{rich(c['title'])}</h1>
      <p class="lead cs__lead">{c['lead']}</p>
      <dl class="glance">
        {glance}
      </dl>
    </div>

    <figure class="wrap cs__figure">
      <div class="frame">
        {c['svg']}
      </div>
      <figcaption>{c['caption']}</figcaption>
    </figure>

    <div class="wrap cs__body">
      <nav class="toc" aria-label="On this page">
        <b>On this page</b>
        <a href="#situation">The situation</a>
        <a href="#problem">The problem</a>
        <a href="#did">What I did</a>
        <a href="#results">Results</a>
        <a href="#learned">What I learned</a>
      </nav>
      <div class="prose">
        <h2 id="situation">The situation</h2>
        {c['situation']}

        <h2 id="problem">The problem</h2>
        {c['problem']}

        <h2 id="did">What I did</h2>
        <ul class="did">
          {did}
        </ul>
        <blockquote class="pull">“{c['quote']}”</blockquote>

        <h2 id="results">Results</h2>
        <div class="results">
          {results}
        </div>

        <h2 id="learned">What I learned</h2>
        {c['learned']}
      </div>
    </div>

    <nav class="wrap cs__next" aria-label="Next case study">
      <small>Next case study</small>
      <a href="{nxt['slug']}.html">{rich(nxt['title'])} →</a>
    </nav>
  </article>
</main>

{FOOT}"""


def main():
    idx = ROOT / "index.html"
    s = idx.read_text()
    start, end = "<!-- WORK:START -->", "<!-- WORK:END -->"
    a, b = s.index(start) + len(start), s.index(end)
    grid = '\n    <div class="work">\n' + "".join(card(c, i == 0) for i, c in enumerate(CASES)) + "    </div>\n"
    idx.write_text(s[:a] + grid + s[b:])
    out = ROOT / "work"
    out.mkdir(exist_ok=True)
    for i, c in enumerate(CASES):
        (out / f"{c['slug']}.html").write_text(page(c, CASES[(i + 1) % len(CASES)]))
    print(f"wrote {len(CASES)} case studies to work/ and the card grid in index.html")


if __name__ == "__main__":
    main()
