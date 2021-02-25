<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Graph</h1>
        <hr />
        <br /><br />

        <br /><br />

        <Plotly :data="data" :layout="layout" :display-mode-bar="true"></Plotly>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { Plotly } from "vue-plotly";

export default {
  data() {
    return {
      polling: null,
      data: [
        {
          x: [],
          y: [],
          type: "scatter",
        },
      ],
      layout: {
        title: "graph",
      },
    };
  },
  components: {
    Plotly,
  },

  methods: {
    getGraphData() {
      const path = "http://localhost:5000/ping/log";
      axios
        .get(path)
        .then((res) => {

          var donnee = [];
          var labelsx = [];
          var values = res.data.values;
          var labels = res.data.labels;

          var tab_data = values.toString().split(",");
          for (var index in tab_data) {
            var tmp = tab_data[index].replace("'", "");
            tmp = tmp.replace("[", "");
            tmp = tmp.replace("]", "");
            tmp = tmp.replace("'", "");
            tmp = tmp.replace("b", "");
            donnee.push(Number(tmp));
          }

          var tab_label = labels.toString().split(",");
          for (var index in tab_label) {
            tmp = tab_label[index].replace("'", "");
            tmp = tmp.replace("[", "");
            tmp = tmp.replace("]", "");
            tmp = tmp.replace("'", "");
            labelsx.push(tmp);
          }

          this.data[0].x = labelsx;
          this.data[0].y = donnee;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    pollData () {
		this.polling = setInterval(() => {
			this.getGraphData()
		}, 3000)
	}
  },
  beforeDestroy () {
	clearInterval(this.polling)
},
  created() {
    this.getGraphData();
    this.pollData()
  },
};
</script>
