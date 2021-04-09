<template>
    <div id="failure">
        <b-alert variant="danger" show>
            Checkout failed! Please try again.
        </b-alert>
        <b-button style="margin-right: 15px;" @click="$router.push('/')">Back to Home</b-button>
    </div>
</template>

<script>
export default {
    name: 'Failure',
}
</script>