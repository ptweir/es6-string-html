# printschedule
app.clientside_callback(
    """
    //js
    function(downloaded_btn) {
        
        if (downloaded_btn !== undefined) {
            if (downloaded_btn > 0) {
                window.print();
            }
        }
        


    }
    ;//!js
    """,
    Output("window_print_output_placeholder", "data"),
    Input('download-btn', 'n_clicks')
)
