import dash_bootstrap_components as dbc
import dash_html_components as html

def Sidebar():

  # the style arguments for the sidebar. We use position:fixed and a fixed width
  SIDEBAR_STYLE = {
      "position": "fixed",
      "top": 60,
      "left": 0,
      "bottom": 0,
      "width": "16rem",
      "padding": "1rem 1rem",
      "background-color": "#f8f9fa",
  }

  sidebar = html.Div(
      [
          html.H4("Sidebar",
                  className="display-4"),
          html.Hr(),
          html.P(
              "A simple sidebar layout with navigation links",
              className="lead"
          ),
          dbc.Nav(
              [
                  dbc.NavLink("Page 1",
                              href="/page-1",
                              id="page-1-link"),
                  dbc.NavLink("Page 2",
                              href="/page-2",
                              id="page-2-link"),
                  dbc.NavLink("Page 3",
                              href="/page-3",
                              id="page-3-link"),
              ],
              vertical=True,
              pills=True,
          ),
      ],
      style=SIDEBAR_STYLE
  )

  return sidebar