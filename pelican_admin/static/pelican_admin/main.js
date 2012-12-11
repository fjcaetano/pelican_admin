/**
 * Created with PyCharm.
 * User: flaviocaetano
 * Date: 11/28/12
 * Time: 8:30 PM
 * To change this template use File | Settings | File Templates.
 */

function pelican_admin(new_status)
{
    if (new_status)
    {
        $('#pelican_status').css('color', 'green').html(gettext('Running'))
        $('#pelican_admin').attr('value', gettext('Stop Service'))
    }
    else
    {
        $('#pelican_status').css('color', 'red').html(gettext('Stopped'))
        $('#pelican_admin').attr('value', gettext('Start Service'))
    }

    $('#pelican_admin').attr('status', new_status)
    $('#pelican_admin').show();
    $('#pelican_loading').hide();

}

window.onload = function() {
    $("#pelican_admin").live('click', function(){

        var status = parseInt(jQuery(this).attr('status'));

        $('#pelican_status').css('color', '#DFA000').html( status ? gettext('Stopping') : gettext('Starting') );
        $('#pelican_admin').hide();
        $('#pelican_loading').show();

        $.ajax({
            url: '/admin/pelican_admin?status='+status,
            dataType: 'jsonp',
            crossDomain: false,
            jsonp: false,
            jsonpCallback: 'pelican_admin'
        });
    });
}