const { createApp, ref } = Vue;

createApp({
  data() {
    return {
      input: "",
      message: [],
    };
  },
  mounted() {
    axios({
      method: "post",
      url: "http://localhost:5005/webhooks/rest/webhook",
      headers: {
        "Content-Type": "application/json",
      },
      data: JSON.stringify({
        sender: "shenzhiqiang",
        message: "你好",
      }),
    }).then((res) => {
      this.message.push(res.data[0]);
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
      axios({
        method: "post",
        url: "http://localhost:5005/webhooks/rest/webhook",
        headers: {
          "Content-Type": "application/json",
        },
        data: JSON.stringify({
          sender: "shenzhiqiang",
          message: text,
        }),
      }).then((res) => {
        this.message.push(res.data[0]);
      });
    },
    clear() {
      this.message = [];
    },
  },
}).mount("#app");
