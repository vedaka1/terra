import { reactive } from "vue";

const user = reactive({
    state: null,
    LogOut() {
        this.state = false
    },
    LogIn () {
        this.state = true
    }
})

export { user }