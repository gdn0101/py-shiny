# Change Log for Shiny (for Python)

All notable changes to Shiny for Python will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [UNRELEASED]

### `input` key changes

* Restored `@render.data_frame`'s (prematurely removed in v0.9.0) input value `input.<ID>_selected_rows()`. Please use `<ID>.input_cell_selection()["rows"]` and consider `input.<ID>_selected_rows()` deprecated. (#1345, #1377)

* `@render.data_frame`'s input value `input.<ID>_data_view_indices` has been renamed to `input.<ID>_data_view_rows` for consistent naming. Please use `input.<ID>_data_view_rows` and consider `input.<ID>_data_view_indices` deprecated. (#1377)

### New features

* Added busy indicators to provide users with a visual cue when the server is busy calculating outputs or otherwise serving requests to the client. More specifically, a spinner is shown on each calculating/recalculating output, and a pulsing banner is shown at the top of the page when the app is otherwise busy. Use the new `ui.busy_indicator.options()` function to customize the appearance of the busy indicators and `ui.busy_indicator.use()` to disable/enable them. (#918)

* Added support for creating modules using Shiny Express syntax, and using modules in Shiny Express apps. (#1220)

* `ui.page_*()` functions gain a `theme` argument that allows you to replace the Bootstrap CSS file with a new CSS file. `theme` can be a local CSS file, a URL, or a [shinyswatch](https://posit-dev.github.io/py-shinyswatch) theme. In Shiny Express apps, `theme` can be set via `express.ui.page_opts()`. (#1334)

### Bug fixes

* Fixed an issue that prevented Shiny from serving the `font.css` file referenced in Shiny's Bootstrap CSS file. (#1342)

* Removed temporary state where a data frame renderer would try to subset to selected rows that did not exist. (#1351, #1377)

### Other changes

* `Session` is now an abstract base class, and `AppSession` is a concrete subclass of it. Also, `ExpressMockSession` has been renamed `ExpressStubSession` and is a concrete subclass of `Session`. (#1331)

* The `Session` class now has a method `is_stub_session()`. For `ExpressStubSession`, this method returns `True` for , and `AppSession` objects it returns `False`. (#1331)

* Closed #1293: The error console would display error messages if an app was disconnected and the user changed an input. (#1339)

* Fixed an issue where some CSS files were larger than necessary because they had source maps embedded in them. (#1339)

## [0.9.0] - 2024-04-16

### Breaking Changes

* `@render.data_frame` return values of `DataTable` and `DataGrid` had their parameter of `row_selection: Literal["single", "multiple"]` become deprecated. Please use `selection_mode="row"` or `selection_mode="rows"` instead. (#1198)

* The `col_widths` argument of `ui.layout_columns()` now sets the `sm` breakpoint by default, rather than the `md` breakpoint. For example, `col_widths=(12, 6, 6)` is now equivalent to `{"sm": (12, 6, 6)}` rather than `{"md": (12, 6, 6)}`. (#1222)

### New features

* `Session` objects now have a `set_message_handler(name, fn)` method that allows you to register a message handler function that will be called when a request message with the given name is received from the client (via `Shiny.shinyapp.makeRequest()` (JS)). (#1253)

* Experimental: `@render.data_frame` return values of `DataTable` and `DataGrid` support `editable=True` to enable editing of the data table cells. (#1198)

* `ui.card()` and `ui.value_box()` now take an `id` argument that, when provided, is used to report the full screen state of the card or value box to the server. For example, when using `ui.card(id = "my_card", full_screen = TRUE)` you can determine if the card is currently in full screen mode by reading the boolean value of `input.my_card_full_screen()`. (#1215, #1266)

* Added support for using `shiny.express` in Quarto Dashboards. (#1217)

* `ui.value_box()`, `ui.layout_columns()` and `ui.layout_column_wrap()` now all have `min_height` and `max_height` arguments. These are useful in filling layouts, like `ui.page_fillable()`, `ui.page_sidebar(fillable=True)` or `ui.page_navbar(fillable=True)`. For example, you can use `ui.layout_columns(min_height=300, max_height=500)` to ensure that a set of items (likely arranged in a row of columns) are always between 300 and 500 pixels tall. (#1223)

* Added an error console which displays errors in the browser's UI. This is enabled by default when running applications locally, and can be disabled with `shiny run --no-dev-mode`. It is not enabled for applications that are deployed to a server. (#1060)

* `shiny create` was updated to include some additional templates as well as an option to choose from the new [templates website](https://shiny.posit.co/py/templates/). (#1273, #1277, #1274)

* `shiny.express.ui.page_opts()` now accepts additional keyword arguments that are passed to the underlying page layout chosen by `shiny.ui.page_auto()`. (#1314)

### Bug fixes

* On Windows, Shiny Express app files are now read in as UTF-8. (#1203)

* `input_dark_mode()` now accepts a `style` argument that can be used to customize the appearance and position of the dark mode toggle switch. (#1207)

* Calling `ui.update_selectize()` with `choices` and `selected` now clears the current selection before updating the choices and selected value. (#1221)

* Fixed an issue that could happen with a `ui.card()` or `ui.value_box()` that is rendered dynamically via `@render.ui` when an updated card replaces a card that the user has expanded into full screen mode. Now the full screen state is reset for the new card or value box. If you want to update a card without potentially exiting the full-screen mode, update specific parts of the card using `ui.output_ui()` or `ui.output_text()`. (#1221)

* `ui.layout_columns()` now correctly applies the `row_heights` at the `xs` breakpoint, if supplied. (#1222)

* `ui.panel_conditional()` now adds the `.shiny-panel-conditional` class to the `<div>` element wrapping the conditional panel contents. (#1257)

* `ui.panel_conditional()` no longer results in unwanted double padding when the parent container uses `gap` for spacing multiple elements (e.g., when used in `ui.layout_columns()`, `ui.page_fillable()`, etc). (#1266)

* Error messages now use `var(--bs-danger)` instead of `var(--bs-danger-text-emphasis)` for the text color. (#1266)

### Other changes

* The fill CSS used by fillable containers (i.e. when `fillable=True`) now uses a [CSS cascade layer](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_layers) named `htmltools` to reduce the precedence order of the fill CSS. (#1228)

## [0.8.1] - 2024-03-06

### Breaking Changes

* `ui.page_sidebar()` now places the `title` element in a `.navbar` container that matches the structure of `page_navbar()`. This ensures that the title elements of `page_sidebar()` and `page_navbar()` have consistent appearance. (#1176)

### Bug fixes

* Shiny now compiles the Bootstrap 5-based stylesheets for component styles imported from https://github.com/rstudio/shiny. (#1191)

* Fixed the CSS for `ui.output_ui()` to avoid unwanted double padding when its parent container uses `gap` for spacing multiple elements (e.g., `ui.layout_columns()`, `ui.page_fillable()`, etc). (#1176)

### Other changes

* Closed #1178: Removed run-time dependency on asgiref. (#1183)

* The uvicorn and click packages are no longer needed when running on Emscripten. (#1187)

* We adjusted the shadows used for cards and popovers. Cards now use a slightly smaller shadow and the same shadow style is also now used by popovers. (#1176)

* We increased the spacing between elements just slightly. This change is most noticeable in the `layout_columns()` or `layout_column_wrap()` component. In these and other components, you can use `gap` and `padding` arguments to choose your own values, or you can set the `$bslib-spacer` (Sass) or `--bslib-spacer` (CSS) variable. (#1176)

## [0.8.0] - 2024-03-04

### Breaking Changes

* Page-level sidebars used in `ui.page_sidebar()` and `ui.page_navbar()` will now default to being initially open but collapsible on desktop devices and always open on mobile devices. You can adjust this default choice by setting `ui.sidebar(open=)`. (#1129)

* `ui.sidebar()` is now a thin wrapper for the internal `ui.Sidebar` class. The `ui.Sidebar` class has been updated to store the sidebar's contents and settings and to delay rendering until the sidebar HTML is actually used. Because most users call `ui.sidebar()` instead of using the class directly, this change is not expected to affect many apps. (#1129)

### New features

* Added `ui.input_dark_mode()`, a toggle switch that allows users to switch between light and dark mode. By default, when `ui.input_dark_mode()` is added to an app, the app's color mode follows the users's system preferences, unless the app author sets the `mode` argument. When `ui.input_dark_mode(id=)` is set, the color mode is reported to the server, and server-side color mode updating is possible using `ui.update_dark_mode()`. (#1149)

* `ui.sidebar(open=)` now accepts a dictionary with keys `desktop` and `mobile`, allowing you to independently control the initial state of the sidebar at desktop and mobile screen sizes. (#1129)

* Closed #984: In Shiny Express apps, if there is a `"www"` subdirectory in the app's directory, Shiny will serve the files in that directory as static assets, mounted at `/`. (#1170)

* For Shiny Express apps, added `express.app_opts()`, which allows setting application-level options, like `static_assets` and `debug`. (#1170)

* Closed #1079: For Shiny Express apps, automatically run a `globals.py` file in the same directory as the app file, if it exists. The code in `globals.py` will be run with the session context set to `None`. (#1172)

### Bug fixes

* Fixed `input_task_button` not working in a Shiny module. (#1108)

* Fixed several issues with `page_navbar()` styling. (#1124)

* Fixed `Renderer.output_id` to not contain the module namespace prefix, only the output id. (#1130)

* Fixed gap-driven spacing between children in fillable `nav_panel()` containers. (#1152)

* Fixed #1138: An empty value in a date or date range input would cause an error; now it is treated as `None`. (#1139)

### Other changes

* `@render.data_frame` now properly fills its container by default. (#1126)

* We improved the accessibility of the full screen toggle button in cards created with `ui.card(full_screen=True)`. Full-screen cards are now also supported on mobile devices. (#1129)

* When entering and exiting full-screen card mode, Shiny now emits a client-side custom `bslib.card` event that JavaScript-oriented users can use to react to the full screen state change. (#1129)

* The sidebar's collapse toggle now has a high `z-index` value to ensure it always appears above elements in the main content area of `ui.layout_sidebar()`. The sidebar overlay also now receives the same high `z-index` on mobile layouts. (#1129)

* Updated example apps to use lower-case versions of `reactive.Calc`->`reactive.calc`, `reactive.Effect`->`reactive.effect`, and `reactive.Value`->`reactive.value`. (#1164)

* Closed #1081: The `@expressify()` function now has an option `has_docstring`. This allows the decorator to be used with functions that contain a docstring. (#1163)

* Replaced use of `sys.stderr.write()` with `print(file=sys.stderr)`, because on some platforms `sys.stderr` can be `None`. (#1131)

* Replaced soon-to-be deprecated `datetime` method calls when handling `shiny.datetime` inputs. (#1146)


## [0.7.1] - 2024-02-05

### Bug fixes

* Fixed `render.download` not working in Express. (#1085)

* `express.ui.hold()` can now accept any type of object, instead of just `TagChild` objects. (#1089)

* Fixed an issue where `input_selectize` would not initialize correctly when created within a Shiny module. (#1091)


## [0.7.0] - 2024-01-25

### Breaking Changes

* Closed #938: `page_sidebar()` and `page_navbar()` now use `fillable=False` by default. (#990)

### New features

* Added `shiny.ui.input_task_button()` for creating buttons that launch longer-running tasks than `shiny.ui.input_action_button()` was designed for. Task buttons give visual feedback that the task is running, and cannot be clicked again until the task is complete. (#907)

* Added `@extended_task` decorator for creating long-running tasks that can be cancelled. (#907)

* Added `@render.download` as a replacement for `@session.download`, which is now deprecated. (#977)

* Added `ui.output_code()`, which is currently an alias for `ui.output_text_verbatim()`. (#997)

* Added `@render.code`, which is an alias for `@render.text`, but in Express mode, it displays the result using `ui.output_code()`. (#997)

* Added `App.on_shutdown` method for registering a callback to be called when the app is shutting down. (#907)

* You can now pass options to `ui.input_selectize` see the [selectize.js](https://selectize.dev/docs/API/selectize) docs for available options. (#914, #158)

* `ui.input_selectize` gains the `remove_button` argument which allows you to control the visibility of the remove button.

### Bug fixes

* CLI command `shiny create`... (#965)
  * has added a `-d`/`--dir` flag for saving to a specific output directory
  * will raise an error if if will overwrite existing files
  * prompt users to install `requirements.txt`

* Fixed `js-react` template build error. (#965)

* Fixed #1007: Plot interaction with plotnine provided incorrect values. (#999)

### Developer features

* Output renderers should now be created with the `shiny.render.renderer.Renderer` class. This class should contain either a `.transform(self, value)` method (common) or a `.render(self)` (rare). These two methods should return something can be converted to JSON. In addition, `.default_ui(self, id)` should be implemented by returning `htmltools.Tag`-like content for use within Shiny Express. To make your own output renderer, please inherit from the `Renderer[IT]` class where `IT` is the type (excluding `None`) required to be returned from the App author. (#964)
  * Legacy renderers that will be removed in the near future:
    * `shiny.render.RenderFunction`
    * `shiny.render.RenderFunctionAsync`
    * `shiny.render.transformer.OutputRenderer`
    * `shiny.render.transformer.OutputRendererSync`
    * `shiny.render.transformer.OutputRendererAsync`

### Other changes

* Pinned Starlette to version <0.35.0; versions 0.35.0 and 0.35.1 caused problems when deploying on Posit Connect. (#1009
)


## [0.6.1.1] - 2023-12-22

### Bug fixes

* Fixed #935: `shiny create` required the `requests` package, but it was not listed as a dependency. It now uses `urllib` instead, which is part of the Python standard library. (#940)


## [0.6.1] - 2023-12-18

### New features

* `shiny create` now allows you to select from a list of template apps.

* `shiny create` provides templates which help you build your own custom JavaScript components.

* Closed #814: The functions `reactive.Calc` and `reactive.Effect` have been changed to have lowercase names: `reactive.calc`, and `reactive.effect`. The old capitalized names are now aliases to the new lowercase names, so existing code will continue to work. Similarly, the class `reactive.Value` has a new alias, `reactive.value`, but in this case, since the original was a class, it keeps the original capitalized name as the primary name. The examples have not been changed yet, but will be changed in a future release. (#822)

* Added `ui.layout_columns()` for creating responsive column-forward layouts based on Bootstrap's 12-column CSS Grid. (#856)

* Added support for Shiny Express apps, which has a simpler, easier-to-use API than the existing API (Shiny Core). Please note that this API is still experimental and may change. (#767)

### Bug fixes

* Fix support for `shiny.ui.accordion(multiple=)` (#799).

### Other changes

* Closed #492: `shiny.ui.nav()` is now deprecated in favor of the more aptly named `shiny.ui.nav_panel()` (#876).

* Update penguins example to credit Allison Horst and drop usage of `shiny.experimental` (#798).

* `as_fillable_container()` and `as_fill_item()` no longer mutate the `Tag` object that was passed in. Instead, it returns a new `Tag` object. Also closed #856: these functions now put the `html-fill-container` and `html-fill-item` CSS classes last, instead of first. (#862)

* `App()` now accepts a server function with a single `input` parameter, or a server function with parameters `input`, `output` and `session`. Server functions with two or more than three parameters now raise an exception. (#920)


## [0.6.0] - 2023-10-30

### Breaking Changes

* `shiny.run` only allows positional arguments for `app`, `host`, and `port`, all other arguments must be specified with keywords.

### New features

* `shiny run` now takes `reload-includes` and `reload-excludes` to allow you to define which files trigger a reload (#780).

* `shiny.run` now passes keyword arguments to `uvicorn.run` (#780).

* The `@output` decorator is no longer required for rendering functions; `@render.xxx` decorators now register themselves automatically. You can still use `@output` explicitly if you need to set specific output options (#747, #790).

* Added support for integration with Quarto (#746).

* Added `shiny.render.renderer_components` decorator to help create new output renderers (#621).

* Added `shiny.experimental.ui.popover()`, `update_popover()`, and `toggle_popover()` for easy creation (and server-side updating) of [Bootstrap popovers](https://getbootstrap.com/docs/5.3/components/popovers/). Popovers are similar to tooltips, but are more persistent, and should primarily be used with button-like UI elements (e.g. `input_action_button()` or icons) (#680).

* Added CSS classes to UI input methods (#680) .

* `Session` objects can now accept an asynchronous (or synchronous) function for `.on_flush(fn=)`, `.on_flushed(fn=)`, and `.on_ended(fn=)` (#686).

* `App()` now allows `static_assets` to represent multiple paths. To do this, pass in a dictionary instead of a string (#763).

* The `showcase_layout` argument of `value_box()` now accepts one of three character values: `"left center"`, `"top right"`, `"bottom"`. (#772)

* `value_box()` now supports many new themes and styles, or fully customizable themes using the new `value_box_theme()` function. To reflect the new capabilities, we've replaced `theme_color` with a new `theme` argument. The previous argument will continue work as expected, but with a deprecation warning. (#772)

  In addition to the Bootstrap theme names (`primary` ,`secondary`, etc.), you can now use the main Boostrap colors (`purple`, `blue`, `red`, etc.). You can also choose to apply the color to the background or foreground by prepending a `bg-` or `text-` prefix to the theme or color name. Finally, we've also added new gradient themes allowing you to pair any two color names as `bg-gradient-{from}-{to}` (e.g., `bg-gradient-purple-blue`).

  These named color themes aren't limited to value boxes: because they're powered by small utility classes, you can use them anywhere within your bslib-powered UI.

* Added `shiny.ui.showcase_bottom()`, a new `shiny.ui.value_box()` layout that places the showcase below the value box `title` and `value`, perfect for a full-bleed plot. (#772)

### Bug fixes

* `shiny run` now respects the user provided `reload-dir` argument (#765).

* Fixed #646: Wrap bare value box value in `<p />` tags. (#668)

* Fixed #676: The `render.data_frame` selection feature was underdocumented and buggy (sometimes returning `None` as a row identifier if the pandas data frame's index had gaps in it). With this release, the selection is consistently a tuple of the 0-based row numbers of the selected rows--or `None` if no rows are selected. (#677)

* Added tests to verify that ui input methods, ui labels, ui update (value) methods, and ui output methods work within modules (#696).

* Adjusted the `@render.plot` input type to be `object` to allow for any object (if any) to be returned (#712).

* In `layout_column_wrap()`, when `width` is a CSS unit -- e.g. `width = "400px"` or `width = "25%"` -- and `fixed_width = FALSE`, `layout_column_wrap()` will ensure that the columns are at least `width` wide, unless the parent container is narrower than `width`. (#772)

### Other changes

* `input_action_button()` now defaults to having whitespace around it. (#758)

* `layout_sidebar()` now uses an `<aside>` element for the sidebar's container and a `<header>` element for the sidebar title. The classes of each element remain the same, but the semantic meaning of the elements is now better reflected in the HTML markup.  (#772)

* `layout_sidebar()` no longer gives the sidebar main content area the `role="main"` attribute. (#772)

* Improved the style and appearance of the button to enter full screen in `card()`s and `value_box()`es to better adapt to Bootstrap's dark mode. (#772)

### API changes

* Added `shiny.ui.navset_underline()` and `shiny.ui.navset_card_underline()` whose navigation container is similar to `shiny.ui.navset_tab()` and `shiny.ui.navset_card_tab()` respectively, but its active/focused navigation links are styled with an underline. (#772)

* `shiny.ui.layout_column_wrap(width, *args)` was rearranged to `shiny.ui.layout_column_wrap(*args, width)`. Now, `width` will default to `200px` is no value is provided. (#772)

* `shiny.ui.showcase_left_center()` and `shiny.ui.showcase_top_right()` no longer take two values for the `width` argument. Instead, they now take a single value (e.g., `width = "30%"`) representing the width of the showcase are in the value box. Furthermore, they've both gained `width_full_screen` arguments that determine the width of the showcase area when the value box is expanded to fill the screen. (#772)

* `shiny.ui.panel_main()` and `shiny.ui.panel_sidebar()` are deprecated in favor of new API for `shiny.ui.layout_sidebar()`. Please use `shiny.ui.sidebar()` to construct a `sidebar=` and supply it to `shiny.ui.layout_sidebar(sidebar, *args, **kwargs)`. (#788)

* `shiny.experimental.ui.toggle_sidebar()` has been renamed to `shiny.ui.update_sidebar()`. It's `open` value now only supports `bool` values. (#788)

#### API relocations

* `shiny.ui`'s `navset_pill_card()` and `navset_tab_card()` have been renamed to `navset_card_pill()` and `navset_card_tab()` respectively (#492).

The following methods have been moved from `shiny.experimental.ui` and integrated into `shiny.ui` (final locations under `shiny.ui` are displayed) (#680):

* Sidebar - Sidebar layout or manipulation
  * `sidebar()`, `page_sidebar()`, `update_sidebar()`, `layout_sidebar()`, `Sidebar`

* Filling layout - Allow UI components to expand into the parent container and/or allow its content to expand
  * `page_fillable()`, `fill.as_fillable_container()`, `fill.as_fill_item()`, `fill.remove_all_fill()`
  * `output_plot(fill=)`, `output_image(fill=)`, `output_ui(fill=, fillable=)`

* CSS units - CSS units and padding
  * `css.as_css_unit()`, `css.as_css_padding()`, `css.CssUnit`

* Tooltip - Hover-based context UI element
  * `tooltip()`, `update_tooltip()`

* Popover - Click-based context UI element
  * `popover()`, `update_popover()`

* Accordion - Vertically collapsible UI element
  * `accordion()`, `accordion_panel()`, `insert_accordion_panel()`, `remove_accordion_panel()`, `update_accordion()`, `update_accordion_panel()`, `Accordion`, `AccordionPanel`

* Card - A general purpose container for grouping related UI elements together
  * `card()`, `card_header()`, `card_footer()`, `CardItem`

* Valuebox - Opinionated container for displaying a value and title
  * `valuebox()`
  * `showcase_left_center()`
  * `showcase_top_right()`

* Navs - Navigation within a page
  * `navset_bar()`, `navset_tab_card()`, `navset_pill_card()`
  * `page_navbar(sidebar=, fillable=, fillable_mobile=, gap=, padding=)`, `navset_card_tab(sidebar=)`, `navset_card_pill(sidebar=)`, `navset_bar(sidebar=, fillable=, gap=, padding=)`

* Layout - Layout of UI elements
  * `layout_column_wrap()`

* Inputs - UI elements for user input
  * `input_text_area(autoresize=)`

If a ported method is called from `shiny.experimental.ui`, a deprecation warning will be displayed.

Methods still under consideration in `shiny.experimental.ui`:

* `card(wrapper=)`: A function (which returns a UI element) to call on unnamed arguments in `card(*args)` which are not already `shiny.ui.CardItem` objects.

* `card_body()`: A container for grouping related UI elements together

* `card_image()`: A general container for an image within a `shiny.ui.card`.

* `card_title()`: A general container for the "title" of a `shiny.ui.card`.

#### API removals

* `shiny.experimental.ui.FillingLayout` has been removed. (#481)

* `shiny.experimental.ui.toggle_switch()` has been made defunct. Please remove it from your code and use `shiny.ui.update_switch()` instead. (#772)

* `shiny.experimental.ui.as_width_unit()` has been made defunct. Please remove it from your code. (#772)

* `shiny.experimental.ui`' `as_fill_carrier()`, `is_fill_carrier()`, `is_fillable_container()`, and `is_fill_item()` have been made defunct. Remove them from your code. (#680, #788)

* Support for `min_height=`, `max_height=`, and `gap=` in `shiny.experimental.ui.as_fillable_container()` and `as_fill_item()` has been removed. (#481)

* `shiny.experimental.ui.TagCallable` has been made defunct. Please use its type is equivalent to `htmltools.TagFunction`. (#680)


## [0.5.1] - 2023-08-08

### Bug fixes

* Fixed #666: Added missing sidebar stylesheet dependency. (#667)


## [0.5.0] - 2023-08-01

### New features

* The new fast-scrolling data table/grid feature (`ui.output_data_frame`/`render.data_frame`) now has a filtering feature. To enable, pass the argument `filters=True` to the `render.DataTable` or `render.DataGrid` constructors. (#592)

* `shiny run` now takes a `--reload-dir <DIR>` argument that indicates a directory `--reload` should (recursively) monitor for changes, in addition to the app's parent directory. Can be used more than once. (#353)

* The default theme has been updated to use Bootstrap 5 with custom Shiny style enhancements. (#624)

* Added experimental UI `tooltip()`, `update_tooltip()`, and `toggle_tooltip()` for easy creation (and server-side updating) of [Bootstrap tooltips](https://getbootstrap.com/docs/5.2/components/tooltips/) (a way to display additional information when focusing (or hovering over) a UI element). (#629)


### Bug fixes

* Using `update_slider` to update a slider's value to a `datetime` object or other non-numeric value would result in an error. (#649)

### Other changes

* Documentation updates. (#591)

* Removed Python 3.7 support. (#590)


## [0.4.0] - 2023-06-26

### New features

* Added new fast-scrolling data table and data grid outputs. (#538)

* Added `include_js()` and `include_css()`, for easily including JS and CSS files in an application. (#127)

* Added sidebar, card, value box, and accordion methods into `shiny.experimental.ui`. (#481)

* Added `fill` and `fillable` methods into `shiny.experimental.ui`. If `fill` is `True`, then the UI component is allowed to expand into the parent container. If `fillable` is `True`, then the UI component will allow its content to expand. Both `fill` on the child component and `fillable` on the parent component must be `True` for the child component to expand. (#481)

* Added sidebar methods into `shiny.experimental.ui`. `shiny.experimental.ui.layout_sidebar()` does not require `ui.panel_main()` and `ui.panel_sidebar()`. These two methods have been deprecated. `x.ui.page_navbar()`, `x.ui.navset_bar()`, `x.navset_tab_card()`, and `x.navset.pill_card()` added `sidebar=` support. (#481)

* feat(sidebar): `ui.layout_sidebar()` internally uses `x.ui.layout_sidebar()`, enabling filling layout features. (#568)


### Bug fixes

* Fixed #496: Previously, when `shiny run --reload` was used, the app would only reload when a .py file changed. Now it will reload when .py, .css, .js, and .html files change. (#505)

* Closed #535: Added a meta viewport tag, so that page layout will adapt to mobile device screens. (#540)

## [0.3.3] - 2023-04-26

### New features

* Added `shiny.experimental` as a place to put experimental features. When using Shiny's experimental features, we recommend importing them by calling `import shiny.experimental as x`, so that all local function calls must start with `x` (e.g. `x.ui.card()`) to signify the method may be changed/removed without warning or future support. (#462)

* Added `penguins` example. (#462)

* The bootstrap HTMLDependency is now created using the dev version of `{bslib}` to get the latest features. (#462)

* Added `shiny.experimental.ui.input_text_area()`, which supports auto-resizing height to fit the content when `autoresize=True`. (#463)

### Other changes

* `shiny.reactive.lock` is now exported. (#458)

## [0.3.2] - 2023-04-19

### Bug fixes

* Fixed #456: plot interaction with datetimes raised errors on 32-bit platforms. (#457)

### Other changes

* When pyright creates type stubs for shiny, it now will include types imported in `_typing_extensions.py`.


## [0.3.1] - 2023-04-18

### Bug fixes

* Fixed #443: Errors in streaming downloads previously resulted in a partially downloaded file; now Shiny responds with a `Transfer-Encoding: chunked` header, which allows the browser to detect the error and abort the download. (#447)

### Other changes

* `page_navbar` now accepts shinyswatch themes. (#455)


## [0.3.0] - 2023-04-03

### New features

* Added support for URL based HTMLDependencies. `{htmltools}` (v0.1.5.9001) added support for URL based HTMLDependencies in rstudio/py-htmltools#53.  (#437)


## [0.2.10] - 2023-03-11

### New features

* Added support for interacting with plots made with matplotlib, seaborn, and plotnine. (#392)

* The `req()` function now returns its first argument (assuming none of its arguments are falsey). This lets you perform validation on expressions as you assign, return, or pass them, without needing to introduce a separate statement just to call `req()`.

* Added `Input.__contains__` method, so that (for example) one could write an expression like `if "x" in inputs`. (#402)

### Bug fixes

* The `width` parameters for `input_select` and `input_slider` now work properly. (Thanks, @bartverweire!) (#386)

* When `input_select` or `input_selectize` were not given an explicit `select` argument, they always chose the first item, which is correct when `multiple=False`, but not when `multiple=True`. Now when `multiple=True`, the first item is no longer automatically selected. (#396)

### Other changes

* Switched to new types from htmltools 0.1.5. (#416)


## [0.2.9] - 2022-11-03

### Bug fixes

* Closed #240, #330: Fixed live examples with additional files. (#340)

* Fixed `shiny run` handling on Windows of absolute paths with drive letter, as in `shiny run c:/myapp/app.py`. (#370)


## [0.2.8] - 2022-10-20

### Bug fixes

* `panel_conditional` now works correctly inside of Shiny modules. (Thanks, @gcaligari!) (#336)

* Fix compatibility with Uvicorn 0.19.0 (#357)


## [0.2.7] - 2022-09-27

### New features

* `shiny run` now takes a `--launch-browser` argument that causes the default web browser to be launched after the app is successfully loaded. Also, the `--port` argument now interprets a value of `0` as "listen on a random port". (#329)

### Other changes

* Updated API document generation with updated paths to work with new version of Shinylive. (#331)


## [0.2.6] - 2022-09-02

### New features

* Closed [#312](https://github.com/posit-dev/py-shiny/issues/312): Matplotlib plots in a `@render.plot` can now use the global figure, instead of returning a `figure` object. ([#314](https://github.com/posit-dev/py-shiny/pull/314))

* Disabled `shiny static` command, in favor of `shinylive export` from the shinylive package. ([#326](https://github.com/posit-dev/py-shiny/pull/326))


## [0.2.5] - 2022-08-12

### New features

* Closed [#269](https://github.com/posit-dev/py-shiny/issues/269): The UI for a `shiny.App` object can now be provided as a function. ([#299](https://github.com/posit-dev/py-shiny/pull/299))

* When a Shinylive deployment is made with `shiny static`, it the deployment code is now delegated to Shinylive. ([#310](https://github.com/posit-dev/py-shiny/pull/310))

### Bug fixes

* Fixed [#279](https://github.com/posit-dev/py-shiny/issues/279): When a Shiny application is mounted to a Starlette route, reactivity did not work. ([#294](https://github.com/posit-dev/py-shiny/pull/294))

* Fixed [#290](https://github.com/posit-dev/py-shiny/issues/290): `@render.plot` now works as intended inside `@module.server`. ([#292](https://github.com/posit-dev/py-shiny/pull/292))

* Fixed [#289](https://github.com/posit-dev/py-shiny/issues/289): `input_selectize()` now resolves the input id before using for other id-like attributes ([#291](https://github.com/posit-dev/py-shiny/pull/291))

## [0.2.4] - 2022-08-01

### Bug fixes

* Fixed [#287](https://github.com/posit-dev/py-shiny/issues/287): Running `shiny static` on Windows failed with `PermissionError`. ([#288](https://github.com/posit-dev/py-shiny/pull/288))

## [0.2.3] - 2022-07-28

### Bug fixes

* Fixed [#281](https://github.com/posit-dev/py-shiny/issues/281): Directory creation for Shinylive assets could fail if the parent directory did not exist. ([#283](https://github.com/posit-dev/py-shiny/pull/283))

## [0.2.2] - 2022-07-27

Initial release of Shiny for Python https://shiny.posit.co/py/
