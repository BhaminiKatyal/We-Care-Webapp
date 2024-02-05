const localVideo = document.getElementById('localVideo');
const remoteVideo = document.getElementById('remoteVideo');
const joinButton = document.getElementById('joinButton');
const leaveButton = document.getElementById('leaveButton');

let localStream;
let remoteStream;
let rtcPeerConnection;

const iceServers = {
    iceServers: [
        { urls: 'stun:stun.l.google.com:19302' },
        // Add more servers if needed
    ],
};

const streamConstraints = { audio: true, video: true };

joinButton.addEventListener('click', joinCall);
leaveButton.addEventListener('click', leaveCall);

async function joinCall() {
    try {
        localStream = await navigator.mediaDevices.getUserMedia(streamConstraints);
        localVideo.srcObject = localStream;

        rtcPeerConnection = new RTCPeerConnection(iceServers);
        rtcPeerConnection.addStream(localStream);

        rtcPeerConnection.onicecandidate = onIceCandidate;
        rtcPeerConnection.onaddstream = onAddStream;

        const offer = await rtcPeerConnection.createOffer();
        await rtcPeerConnection.setLocalDescription(offer);

        // Send the offer to the other peer (You need a signaling server for this part)

    } catch (error) {
        console.error('Error joining call:', error);
    }
}

function onIceCandidate(event) {
    if (event.candidate) {
        // Send the candidate to the other peer (via signaling server)
    }
}

async function onAddStream(event) {
    remoteVideo.srcObject = event.stream;
    remoteStream = event.stream;
}

function leaveCall() {
    if (rtcPeerConnection) {
        rtcPeerConnection.close();
    }
    if (localStream) {
        localStream.getTracks().forEach(track => track.stop());
    }
    localVideo.srcObject = null;
    remoteVideo.srcObject = null;
}