(() => {
  const nav = document.querySelector("[data-nav]");
  if (nav) {
    const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 8);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
  const select = (tab) => {
    tabs.forEach((t) => {
      const on = t === tab;
      t.setAttribute("aria-selected", String(on));
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute("aria-controls")).hidden = !on;
    });
    tab.focus();
  };
  tabs.forEach((tab, i) => {
    tab.addEventListener("click", () => select(tab));
    tab.addEventListener("keydown", (e) => {
      const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
      if (step) {
        e.preventDefault();
        select(tabs[(i + step + tabs.length) % tabs.length]);
      }
    });
  });

  const filters = document.querySelector("[data-filters]");
  const list = document.querySelector("[data-projects]");
  if (filters && list) {
    const buttons = Array.from(filters.querySelectorAll("button"));
    const items = Array.from(list.querySelectorAll("[data-kind]"));
    const status = document.querySelector("[data-status]");
    buttons.forEach((btn) =>
      btn.addEventListener("click", () => {
        const kind = btn.dataset.filter;
        buttons.forEach((b) => b.setAttribute("aria-pressed", String(b === btn)));
        let shown = 0;
        items.forEach((el) => {
          const match = kind === "all" || el.dataset.kind === kind;
          el.hidden = !match;
          if (match) shown += 1;
        });
        if (status) status.textContent = `Showing ${shown} ${shown === 1 ? "project" : "projects"}`;
      })
    );
  }
})();
