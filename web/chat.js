const { createApp, ref } = Vue;

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
        this.message.push(res.data[0]);
      });
    },
  },
}).mount("#app");
