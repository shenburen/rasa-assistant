const { createApp, ref } = Vue;

createApp({
  setup() {
    const input = ref("123");
    const message = ref([
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
      {
        sender: "shenzhiqiang",
        message: "你好",
      },
      {
        recipient_id: "shenzhiqiang",
        text: "我很好",
      },
    ]);
    return {
      input,
      message,
    };
  },
  methods: {
    submit() {
      alert(1);
    },
    clear() {},
  },
}).mount("#app");
