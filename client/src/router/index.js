import Vue from 'vue';
import Router from 'vue-router';
import Graph from '../components/Graph.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Graph',
      component: Graph,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});
