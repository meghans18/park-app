<template>
    <div id="return">
        Returning to site...
    </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from "vuex";

export default {
    name: 'Return',
    methods: {
        ...mapActions(["connect"]),
        checkConnection() {
            let userEmail = this.$store.getters.getEmail
            const path = `http://localhost:5000/is-connected/${userEmail}`
            axios.get(path).then((response) => {
                if (response.data.acct_info.details_submitted) {
                    const payload = {
                        'connected': 'yes'
                    }
                    this.connect(payload);
                } else {
                    const payload = {
                        'connected': 'partly'
                    }
                    this.connect(payload);
                }
                this.$router.push('/manage-spots-owned')
            })
        }
    },
    mounted: function() {
        this.checkConnection();
    }
}
</script>