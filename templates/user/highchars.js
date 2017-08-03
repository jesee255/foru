var log = console.log.bind(console)

var formatData = function (data) {
    var l = []
    for (var i = 0; i < data.length; i++) {
        var m = data[i]
        var d = {
            'message': m.message,
            'occur_time': m.occur_time,
            'is_send': m.is_send,
            'create_time': m.create_time,
        }
        l.push(d)
    }
    return l
}

$.getJSON('/uploads/read_profile', {}, function (raw) {
    if (raw) {
        log('raw', raw)
        tableInit(raw)
    }
})
var tableInit = function (data) {
    $('#table').bootstrapTable('destroy').bootstrapTable({
        columns: [{
            checkbox: true
        }, {
            field: 'message',
            title: 'message'
        }, {
            field: 'occur_time',
            title: 'occur_time'
        }, {
            field: 'is_send',
            title: 'is_send'
        }, {
            field: 'create_time',
            title: 'create_time'
        }],
        data: data
    });
}