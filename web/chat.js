const { createApp } = Vue;

createApp({
  data() {
    return {
      input: "",
      message: [],
    };
  },
  mounted() {
    this.postMessage({
      sender: "shenzhiqiang",
      message: "你好",
    });
  },
  methods: {
    submit() {
      let text = this.input;
      this.input = "";
      this.message.push({
        sender: "shenzhiqiang",
        message: text,
      });
      this.postMessage({
        sender: "shenzhiqiang",
        message: text,
      });
    },
    clear() {
      this.message = [];
    },
    postMessage(obj) {
      axios({
        method: "post",
        url: "http://localhost:5005/webhooks/rest/webhook",
        headers: {
          "Content-Type": "application/json",
        },
        data: JSON.stringify(obj),
      }).then((res) => {
        if (res.data.length < 1) {
          return;
        }
        let result = this.checkMessage(res.data[0]);
        if (!result.json) {
          this.message.push(result);
        } else {
          result.class = result.json.type + (this.message.length + 1);
          this.message.push({
            echarts: result.class,
          });
          setTimeout(() => {
            this.createEcharts(result);
          }, 0);
        }
      });
    },
    checkMessage(message) {
      let result = message;
      try {
        result.json = JSON.parse(message.text);
      } catch (error) {
        console.info(error);
      }
      return result;
    },
    createEcharts(result) {
      let dom = document.querySelector("." + result.class);
      let chart = echarts.init(dom);

      let option = {
        calendar: [
          {
            left: "center",
            top: "middle",
            cellSize: [50, 50],
            yearLabel: { show: false },
            orient: "vertical",
            dayLabel: {
              firstDay: 1,
              nameMap: "cn",
            },
            monthLabel: {
              show: false,
            },
            range: "2024-6",
          },
        ],
        series: [
          // 休息日
          {
            type: "scatter",
            coordinateSystem: "calendar",
            symbolSize: 0,
            label: {
              show: true,
              formatter: function (params) {
                var d = echarts.number.parseDate(params.value[0]);
                var l = params.value[1];
                if (l == "") {
                  return "\n\n" + d.getDate() + "\n\n" + l + "\n\n";
                } else {
                  return "";
                }
              },
              color: "#000",
            },
            data: result.json.list,
            silent: true,
          },
          // 打卡正常
          {
            type: "scatter",
            coordinateSystem: "calendar",
            symbolSize: 0,
            label: {
              show: true,
              formatter: function (params) {
                var d = echarts.number.parseDate(params.value[0]);
                var l = params.value[1];
                if (l == "正常") {
                  return "\n\n" + d.getDate() + "\n\n" + l + "\n\n";
                } else {
                  return "";
                }
              },
              color: "#67c23a",
            },
            data: result.json.list,
            silent: true,
          },
          // 打卡异常
          {
            type: "scatter",
            coordinateSystem: "calendar",
            symbolSize: 0,
            label: {
              show: true,
              formatter: function (params) {
                var d = echarts.number.parseDate(params.value[0]);
                var l = params.value[1];
                if (l == "异常") {
                  return "\n\n" + d.getDate() + "\n\n" + l + "\n\n";
                } else {
                  return "";
                }
              },
              color: "#e6a23c",
            },
            data: result.json.list,
            silent: true,
          },
          // 缺卡
          {
            type: "scatter",
            coordinateSystem: "calendar",
            symbolSize: 0,
            label: {
              show: true,
              formatter: function (params) {
                var d = echarts.number.parseDate(params.value[0]);
                var l = params.value[1];
                if (l == "缺卡") {
                  return "\n\n" + d.getDate() + "\n\n" + l + "\n\n";
                } else {
                  return "";
                }
              },
              color: "#f56c6c",
            },
            data: result.json.list,
            silent: true,
          },
        ],
      };

      chart.setOption(option);
    },
  },
}).mount("#app");
