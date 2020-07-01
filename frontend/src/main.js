import Vue from 'vue'
import App from './App.vue'
import {BootstrapVue} from 'bootstrap-vue'
import {createProvider} from './vue-apollo'
import Cookies from 'js-cookie';

Vue.use(BootstrapVue)

Vue.config.productionTip = false


new Vue({
    apolloProvider: createProvider({
        request: (operation) => {
            operation.setContext({
                headers: {
                    "X-CSRFToken": Cookies.get('csrftoken')
                }
            })
        }
    }),
    render: h => h(App)
}).$mount('#app')
