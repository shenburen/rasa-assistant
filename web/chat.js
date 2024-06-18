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
  },
}).mount("#app");
