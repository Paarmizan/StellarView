import VueRouter from 'vue-router'
import MainPage from "./pages/MainPage.vue";

export default new VueRouter({
    routes: [
        {
            path: '/',
            component: MainPage
        }
    ],
    mode: 'history'
})